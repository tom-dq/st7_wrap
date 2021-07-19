# Friendly wrapper around the Strand7 API.


import tempfile
import dataclasses
import enum
import typing
import ctypes
import pathlib
import collections
import logging

try:
    import numpy

except ImportError:
    logging.warn("Couldn't import numpy - some bits and pieces may not work.")
    numpy = None

import St7API

from st7_wrap.exc import chk
from st7_wrap import arrays
from st7_wrap import const


T_Path = typing.Union[pathlib.Path, str]


class DoF(enum.Enum):
    DX = 0
    DY = 1
    DZ = 2
    RX = 3
    RY = 4
    RZ = 5

    @property
    def rx_mz_text(self) -> str:
        "Return FX, FY, FZ, MX, MY or MZ"
        return self.name.replace("D", "F").replace("R", "M")

    @property
    def is_displacement(self) -> bool:
        return self.value in (0, 1, 2)

    @property
    def disp_or_rotation_text(self) -> str:
        return "Displacement" if self.is_displacement else "Rotation"

    @property
    def force_or_moment_text(self) -> str:
        return "Force" if self.is_displacement else "Moment"


@dataclasses.dataclass
class NodeRestraint:
    node_num: int
    fc_num: int
    ucs_id: int
    restraints: typing.Dict[DoF, float]

    @property
    def global_xyz(self) -> bool:
        return self.ucs_id in {0, 1}


T_XYZ = typing.Sequence[float]


class Vector3(typing.NamedTuple):
    x: float
    y: float
    z: float

    def __radd__(self, other):
        # This is just a convenience so I can use "sum" rather than "reduce with operator.add"...
        if isinstance(other, Vector3):
            return self.__add__(other)

        elif isinstance(other, int):
            if other == 0:
                return self

            else:
                raise ValueError(
                    "Can only add to a zero int, and I probably shouldn't even be doing that."
                )

        else:
            raise TypeError(other)

    def __add__(self, other):
        if not isinstance(other, Vector3):
            raise TypeError(other)

        return Vector3(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z,
        )

    def __sub__(self, other):
        if not isinstance(other, Vector3):
            raise TypeError(other)

        return Vector3(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z,
        )

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(other)

        return Vector3(
            x=self.x / other,
            y=self.y / other,
            z=self.z / other,
        )

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


class StrainTensor(typing.NamedTuple):
    xx: float
    yy: float
    zz: float
    xy: float
    yz: float
    zx: float

    def __radd__(self, other):
        # This is just a convenience so I can use "sum" rather than "reduce with operator.add"...
        if isinstance(other, StrainTensor):
            return self.__add__(other)

        elif isinstance(other, int):
            if other == 0:
                return self

            else:
                raise ValueError(
                    "Can only add to a zero int, and I probably shouldn't even be doing that."
                )

        else:
            raise TypeError(other)

    def __add__(self, other):
        if not isinstance(other, StrainTensor):
            raise TypeError(other)

        return StrainTensor(
            xx=self.xx + other.xx,
            yy=self.yy + other.yy,
            zz=self.zz + other.zz,
            xy=self.xy + other.xy,
            yz=self.yz + other.yz,
            zx=self.zx + other.zx,
        )

    def __sub__(self, other):
        if not isinstance(other, StrainTensor):
            raise TypeError(other)

        return StrainTensor(
            xx=self.xx - other.xx,
            yy=self.yy - other.yy,
            zz=self.zz - other.zz,
            xy=self.xy - other.xy,
            yz=self.yz - other.yz,
            zx=self.zx - other.zx,
        )

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(other)

        return StrainTensor(
            xx=self.xx / other,
            yy=self.yy / other,
            zz=self.zz / other,
            xy=self.xy / other,
            yz=self.yz / other,
            zx=self.zx / other,
        )

    def __abs__(self):
        # Does the max principal make sense as an "abs" value? Not really sure...
        w = numpy.linalg.eigvals(self.as_np_array())
        return max(w)

    def as_np_array(self):
        return numpy.array(
            [
                [self.xx, 0.5 * self.xy, 0.5 * self.zx],
                [0.5 * self.xy, self.yy, 0.5 * self.yz],
                [0.5 * self.zx, 0.5 * self.yz, self.zz],
            ]
        )


class CanvasSize(typing.NamedTuple):
    width: int
    height: int


class ResultOutput(typing.NamedTuple):
    num_points: int
    num_cols: int
    results: typing.Tuple[float]


class AttributeSequenceEntry(typing.NamedTuple):
    ipAttrLocal: int
    ipAttrAxis: int
    ipAttrCase: int
    ipAttrID: int


class TopologicalGraphEdge(enum.Enum):
    """What defines a topological graph edge when exporting data for networkx graphs"""
    node = enum.auto()
    edge = enum.auto()
    face = enum.auto()


class St7Model:
    _fn: str = None
    _temp_dir: str = None
    uID: int = 1

    def __init__(self, fn_st7: T_Path, create_new_model: bool, temp_dir=None):
        self._fn = str(fn_st7)

        if temp_dir:
            self._temp_dir = str(temp_dir)
        else:
            self._temp_dir = tempfile.gettempdir()

        chk(St7API.St7Init())

        if create_new_model:
            chk(St7API.St7NewFile(self.uID, self._fn.encode(), self._temp_dir.encode()))

        else:
            chk(St7API.St7OpenFile(self.uID, self._fn.encode(), self._temp_dir.encode()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        chk(St7API.St7CloseFile(self.uID))
        chk(St7API.St7Release())

    def open_results(self, fn_res: T_Path) -> "St7Results":
        return St7Results(self, fn_res)

    def entity_numbers(self, entity: const.Entity) -> range:
        ct_max_num = ctypes.c_long()
        chk(St7API.St7GetTotal(self.uID, entity.value, ct_max_num))
        return range(1, ct_max_num.value + 1)

    def property_numbers(
        self, entity: typing.Union[const.Property, const.Entity]
    ) -> typing.Iterable[int]:
        ct_arr = ctypes.c_long * 10
        num_props, last_prop = ct_arr(), ct_arr()
        chk(St7API.St7GetTotalProperties(self.uID, num_props, last_prop))

        if entity in (const.Entity.tyBEAM, const.Property.ptBEAMPROP):
            final_prop = num_props[St7API.ipBeamPropTotal]

        elif entity in (const.Entity.tyPLATE, const.Property.ptPLATEPROP):
            final_prop = num_props[St7API.ipPlatePropTotal]

        elif entity in (const.Entity.tyBRICK, const.Property.ptBRICKPROP):
            final_prop = num_props[St7API.ipBrickPropTotal]

        elif entity == const.Property.ptPLYPROP:
            final_prop = num_props[St7API.ipPlyPropTotal]

        else:
            raise ValueError(entity)

        for prop_idx in range(1, final_prop + 1):
            prop_num = ctypes.c_long()
            chk(St7API.St7GetPropertyNumByIndex(self.uID, entity.value, prop_idx, prop_num))
            yield prop_num.value

    def St7NewLoadCase(self, case_name: str):
        chk(St7API.St7NewLoadCase(self.uID, case_name.encode()))

    def St7GetNumLoadCase(self) -> int:
        ct_num_cases = ctypes.c_long()
        chk(St7API.St7GetNumLoadCase(self.uID, ct_num_cases))
        return ct_num_cases.value

    def load_case_numbers(self) -> range:
        return range(1, self.St7GetNumLoadCase() + 1)

    def St7GetNumFreedomCase(self) -> int:
        ct_num_cases = ctypes.c_long()
        chk(St7API.St7GetNumFreedomCase(self.uID, ct_num_cases))
        return ct_num_cases.value

    def freedom_case_numbers(self) -> range:
        return range(1, self.St7GetNumFreedomCase() + 1)

    def St7SetPlatePreLoad3(
        self, iPlate: int, iLoadCase: int, load_type: const.PreLoadType, load: Vector3
    ):
        doubles = (ctypes.c_double * 3)(*load)
        chk(St7API.St7SetPlatePreLoad3(self.uID, iPlate, iLoadCase, load_type.value, doubles))

    def St7RunSolver(self, solver: const.SolverType, solver_mode: const.SolverMode, wait: bool):
        chk(St7API.St7RunSolver(self.uID, solver.value, solver_mode.value, wait))

    def St7EnableNLALoadCase(self, stage: int, load_case_num: int):
        chk(
            St7API.St7EnableNLALoadCase(
                self.uID,
                stage,
                load_case_num,
            )
        )

    def St7DisableNLALoadCase(self, stage: int, load_case_num: int):
        chk(
            St7API.St7DisableNLALoadCase(
                self.uID,
                stage,
                load_case_num,
            )
        )

    def St7EnableNLAFreedomCase(self, stage: int, freedom_case_num: int):
        chk(
            St7API.St7EnableNLAFreedomCase(
                self.uID,
                stage,
                freedom_case_num,
            )
        )

    def St7DisableNLAFreedomCase(self, stage: int, freedom_case_num: int):
        chk(
            St7API.St7DisableNLAFreedomCase(
                self.uID,
                stage,
                freedom_case_num,
            )
        )

    def St7AddNLAIncrement(self, stage: int, inc_name: str):
        chk(St7API.St7AddNLAIncrement(self.uID, stage, inc_name.encode()))

    def St7SetNLALoadIncrementFactor(
        self, stage: int, increment: int, load_case_num: int, factor: float
    ):
        chk(St7API.St7SetNLALoadIncrementFactor(self.uID, stage, increment, load_case_num, factor))

    def St7SetNLAFreedomIncrementFactor(
        self, stage: int, increment: int, freedom_case_num: int, factor: float
    ):
        chk(
            St7API.St7SetNLAFreedomIncrementFactor(
                self.uID, stage, increment, freedom_case_num, factor
            )
        )

    def St7GetNumNLAIncrements(self, stage: int) -> int:
        ct_incs = ctypes.c_long()
        chk(St7API.St7GetNumNLAIncrements(self.uID, stage, ct_incs))
        return ct_incs.value

    def St7EnableSaveRestart(self):
        chk(St7API.St7EnableSaveRestart(self.uID))

    def St7EnableSaveLastRestartStep(self):
        chk(St7API.St7EnableSaveLastRestartStep(self.uID))

    def St7SetNLAInitial(self, fn_res: T_Path, case_num: int):
        chk(St7API.St7SetNLAInitial(self.uID, str(fn_res).encode(), case_num))

    def St7SetQSAInitial(self, fn_res: T_Path, case_num: int):
        chk(St7API.St7SetQSAInitial(self.uID, str(fn_res).encode(), case_num))

    def St7SetResultFileName(self, fn_res: T_Path):
        chk(
            St7API.St7SetResultFileName(
                self.uID,
                str(fn_res).encode(),
            )
        )

    def St7SetStaticRestartFile(self, fn_restart: T_Path):
        chk(
            St7API.St7SetStaticRestartFile(
                self.uID,
                str(fn_restart).encode(),
            )
        )

    def St7EnableTransientLoadCase(self, case_num: int):
        chk(St7API.St7EnableTransientLoadCase(self.uID, case_num))

    def St7DisableTransientLoadCase(self, case_num: int):
        chk(St7API.St7DisableTransientLoadCase(self.uID, case_num))

    def St7EnableTransientFreedomCase(self, case_num: int):
        chk(St7API.St7EnableTransientFreedomCase(self.uID, case_num))

    def St7DisableTransientFreedomCase(self, case_num: int):
        chk(St7API.St7DisableTransientFreedomCase(self.uID, case_num))

    def St7SetTransientLoadTimeTable(self, case_num: int, table_num: int, add_time_steps: bool):
        chk(St7API.St7SetTransientLoadTimeTable(self.uID, case_num, table_num, add_time_steps))

    def St7SetTransientFreedomTimeTable(self, case_num: int, table_num: int, add_time_steps: bool):
        chk(St7API.St7SetTransientFreedomTimeTable(self.uID, case_num, table_num, add_time_steps))

    def St7SaveFile(self):
        chk(St7API.St7SaveFile(self.uID))

    def St7SaveFileCopy(self, fn_st7: str):
        chk(St7API.St7SaveFileCopy(self.uID, str(fn_st7).encode()))

    def St7GetElementCentroid(
        self, entity: const.Entity, elem_num: int, face_edge_num: int
    ) -> Vector3:
        ct_xyz = (ctypes.c_double * 3)()
        chk(St7API.St7GetElementCentroid(self.uID, entity.value, elem_num, face_edge_num, ct_xyz))
        return Vector3(*ct_xyz)

    def St7GetElementData(self, entity: const.Entity, elem_num: int, res_case_num: int) -> float:
        ct_data = ctypes.c_double()
        chk(St7API.St7GetElementData(self.uID, entity.value, elem_num, res_case_num, ct_data))
        return ct_data.value

    def St7GetNodeXYZ(self, node_num: int) -> Vector3:
        ct_xyz = (ctypes.c_double * 3)()
        chk(St7API.St7GetNodeXYZ(self.uID, node_num, ct_xyz))
        return Vector3(*ct_xyz)

    def St7SetNodeXYZ(self, node_num: int, xyz: typing.Union[T_XYZ, Vector3]):
        ct_xyz = (ctypes.c_double * 3)(*xyz)
        chk(St7API.St7SetNodeXYZ(self.uID, node_num, ct_xyz))

    def St7GetElementConnection(
        self, entity: const.Entity, elem_num: int
    ) -> typing.Tuple[int, ...]:
        ct_conn = (ctypes.c_long * 30)()
        chk(St7API.St7GetElementConnection(self.uID, entity.value, elem_num, ct_conn))
        n = ct_conn[0]
        return tuple(ct_conn[1 : 1 + n])

    def St7SetElementConnection(
        self, entity: const.Entity, elem_num: int, prop_num: int, connection: typing.Tuple[int, ...]
    ):
        if len(connection) > 30:
            raise IndexError("What kind of element is that?")

        ct_conn = (ctypes.c_long * (len(connection) + 10))()
        ct_conn[0] = len(connection)
        ct_conn[1 : len(connection) + 1] = connection
        chk(St7API.St7SetElementConnection(self.uID, entity.value, elem_num, prop_num, ct_conn))

    def St7CreateModelWindow(self, dont_really_make: bool = False) -> "St7ModelWindow":
        if dont_really_make:
            return St7ModelWindowDummy(model=self)

        else:
            return St7ModelWindow(model=self)

    def St7SetUseSolverDLL(self, use_dll: bool):
        ct_int = ctypes.c_long(use_dll)
        chk(St7API.St7SetUseSolverDLL(ct_int))

    def St7SetNumTimeStepRows(self, num_rows: int):
        chk(St7API.St7SetNumTimeStepRows(self.uID, num_rows))

    def St7SetTimeStepData(self, row: int, num_steps: int, save_every: int, time_step: float):
        chk(St7API.St7SetTimeStepData(self.uID, row, num_steps, save_every, time_step))

    def St7SetSolverDefaultsLogical(
        self, solver_def_logical: const.SolverDefaultLogical, value: bool
    ):
        chk(St7API.St7SetSolverDefaultsLogical(self.uID, solver_def_logical.value, value))

    def St7SetSolverDefaultsInteger(self, solver_def_int: const.SolverDefaultInteger, value: int):
        chk(St7API.St7SetSolverDefaultsInteger(self.uID, solver_def_int.value, value))

    def _make_table_data_and_validate(self, num_entries: int, doubles: typing.Sequence[float]):
        data = list(doubles)
        if len(data) != num_entries * 2:
            raise ValueError("Mismatch!")

        ct_doubles_type = ctypes.c_double * (2 * num_entries)
        ct_doubles = ct_doubles_type(*data)
        return ct_doubles

    def St7NewTableType(
        self,
        table_type: const.TableType,
        table_id: int,
        num_entries: int,
        table_name: str,
        doubles: typing.Sequence[float],
    ):
        ct_doubles = self._make_table_data_and_validate(num_entries, doubles)
        chk(
            St7API.St7NewTableType(
                self.uID, table_type.value, table_id, num_entries, table_name.encode(), ct_doubles
            )
        )

    def St7SetTableTypeData(
        self,
        table_type: const.TableType,
        table_id: int,
        num_entries: int,
        doubles: typing.Sequence[float],
    ):
        ct_doubles = self._make_table_data_and_validate(num_entries, doubles)
        chk(
            St7API.St7SetTableTypeData(
                self.uID, table_type.value, table_id, num_entries, ct_doubles
            )
        )

    def St7SetPlateXAngle1(self, plate_num: int, ang_deg: float):
        ct_doubles = (ctypes.c_double * 10)()
        ct_doubles[0] = ang_deg

        chk(St7API.St7SetPlateXAngle1(self.uID, plate_num, ct_doubles))

    def St7GetPlateXAngle1(self, plate_num: int) -> float:
        ct_doubles = (ctypes.c_double * 10)()

        chk(St7API.St7GetPlateXAngle1(self.uID, plate_num, ct_doubles))
        return ct_doubles[0]

    def St7GetPlateIsotropicMaterial(self, prop_num: int) -> arrays.PlateIsotropicMaterial:
        doubles = arrays.PlateIsotropicMaterial.get_single_sub_array_of_type(ctypes.c_double)
        doubles_arr = doubles.make_empty_array()

        chk(St7API.St7GetPlateIsotropicMaterial(self.uID, prop_num, doubles_arr))

        doubles_instance = doubles.instance_from_st7_array(doubles_arr)
        return arrays.PlateIsotropicMaterial.instance_from_sub_array_instances(doubles_instance)

    def St7SetPlateIsotropicMaterial(
        self, prop_num: int, plate_isotropic_material: arrays.PlateIsotropicMaterial
    ):
        doubles_arr = plate_isotropic_material.get_single_sub_array_instance_of_type(
            ctypes.c_double
        ).to_st7_array()
        chk(St7API.St7SetPlateIsotropicMaterial(self.uID, prop_num, doubles_arr))

    def St7GetEntityAttributeSequence(
        self, entity: const.Entity, entity_num: int, attribute_type: const.AttributeType
    ) -> typing.Iterable[AttributeSequenceEntry]:

        num_sets = ctypes.c_long()
        chk(
            St7API.St7GetEntityAttributeSequenceCount(
                self.uID, entity.value, entity_num, attribute_type.value, num_sets
            )
        )

        arr_size = 4 * (num_sets.value + 10)
        ct_arr = (ctypes.c_long * arr_size)()

        chk(
            St7API.St7GetEntityAttributeSequence(
                self.uID, entity.value, entity_num, attribute_type.value, num_sets, ct_arr
            )
        )

        for i in range(num_sets.value):
            yield AttributeSequenceEntry(
                ipAttrLocal=ct_arr[4 * i + St7API.ipAttrLocal],
                ipAttrAxis=ct_arr[4 * i + St7API.ipAttrAxis],
                ipAttrCase=ct_arr[4 * i + St7API.ipAttrCase],
                ipAttrID=ct_arr[4 * i + St7API.ipAttrID],
            )

    def St7GetNodeRestraint6(self, node_num: int, fc_num: int) -> NodeRestraint:
        ucs_id = ctypes.c_long()
        ct_status = (ctypes.c_long * 6)()
        ct_doubles = (ctypes.c_double * 6)()

        chk(St7API.St7GetNodeRestraint6(self.uID, node_num, fc_num, ucs_id, ct_status, ct_doubles))

        restraint_dict = {DoF(idx): ct_doubles[idx] for idx in range(6) if ct_status[idx]}

        return NodeRestraint(
            node_num=node_num,
            fc_num=fc_num,
            ucs_id=ucs_id.value,
            restraints=restraint_dict,
        )

    def all_node_restraints(self) -> typing.Iterable[NodeRestraint]:
        for node_num in self.entity_numbers(const.Entity.tyNODE):
            for attr_seq_entry in self.St7GetEntityAttributeSequence(
                const.Entity.tyNODE, node_num, const.AttributeType.aoRestraint
            ):
                yield self.St7GetNodeRestraint6(node_num, attr_seq_entry.ipAttrCase)


class St7NewFile(St7Model):
    def __init__(self, fn_st7: T_Path, temp_dir=None):
        create_new_model = True

        super().__init__(fn_st7, create_new_model, temp_dir)


class St7OpenFile(St7Model):
    def __init__(self, fn_st7: T_Path, temp_dir=None):
        create_new_model = False

        super().__init__(fn_st7, create_new_model, temp_dir)


class St7Results:
    model: St7Model = None
    fn_res: str = None
    uID: int = None
    primary_cases: range = None

    def __init__(self, model: St7Model, fn_res: T_Path):

        self.model = model
        self.fn_res = str(fn_res)
        self.uID = self.model.uID

        ct_num_prim, ct_num_sec = ctypes.c_long(), ctypes.c_long()
        chk(
            St7API.St7OpenResultFile(
                self.uID, self.fn_res.encode(), b"", False, ct_num_prim, ct_num_sec
            )
        )

        self.primary_cases = range(1, ct_num_prim.value + 1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        chk(St7API.St7CloseResultFile(self.uID))

    def St7GetNodeResult(
        self,
        res_type: const.NodeResultType,
        node_num: int,
        res_case: int,
    ) -> ResultOutput:
        ct_res_array = (ctypes.c_double * 6)()

        chk(St7API.St7GetNodeResult(self.uID, res_type.value, node_num, res_case, ct_res_array))

        out_array = tuple(ct_res_array)

        return ResultOutput(
            num_points=1,
            num_cols=6,
            results=out_array,
        )

    def St7GetPlateResultArray(
        self,
        res_type: const.PlateResultType,
        res_sub_type: typing.Union[const.PlateResultSubType, int],
        plate_num: int,
        case_num: int,
        sample_location: const.SampleLocation,
        surface: const.PlateSurface,
        layer: int,
    ) -> ResultOutput:

        if isinstance(res_sub_type, const.PlateResultSubType):
            real_sub_type = res_sub_type.value

        elif isinstance(res_sub_type, int):
            real_sub_type = res_sub_type

        else:
            raise TypeError(res_sub_type)

        ct_res_array = (ctypes.c_double * St7API.kMaxPlateResult)()
        ct_num_points = ctypes.c_long()
        ct_num_cols = ctypes.c_long()

        chk(
            St7API.St7GetPlateResultArray(
                self.uID,
                res_type.value,
                real_sub_type,
                plate_num,
                case_num,
                sample_location.value,
                surface.value,
                layer,
                ct_num_points,
                ct_num_cols,
                ct_res_array,
            )
        )

        out_array = tuple(ct_res_array[0 : ct_num_points.value * ct_num_cols.value])
        return ResultOutput(
            num_points=ct_num_points.value,
            num_cols=ct_num_cols.value,
            results=out_array,
        )


class St7ModelWindow:
    model: St7Model = None
    uID: int = None

    def __init__(self, model: St7Model):
        self.model = model
        self.uID = self.model.uID
        chk(St7API.St7CreateModelWindow(self.uID))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Don't check for an error here.
        St7API.St7DestroyModelWindow(self.uID)

    def close(self):
        chk(St7API.St7DestroyModelWindow(self.uID))

    def St7ShowModelWindow(self):
        chk(St7API.St7ShowModelWindow(self.uID))

    def St7DestroyModelWindow(self):
        chk(St7API.St7DestroyModelWindow(self.uID))

    def St7GetDrawAreaSize(self) -> CanvasSize:
        ct_width, ct_height = ctypes.c_long(), ctypes.c_long()
        chk(St7API.St7GetDrawAreaSize(self.uID, ct_width, ct_height))
        return CanvasSize(width=ct_width.value, height=ct_height.value)

    def St7PositionModelWindow(self, left: int, top: int, width: int, height: int):
        chk(St7API.St7PositionModelWindow(self.uID, left, top, width, height))

    def St7SetEntityContourIndex(
        self,
        entity: const.Entity,
        index: typing.Union[const.BeamContour, const.PlateContour, const.BrickContour],
    ):
        chk(St7API.St7SetEntityContourIndex(self.uID, entity.value, index.value))

    def St7ExportImage(self, fn: T_Path, image_type: const.ImageType, width: int, height: int):
        chk(St7API.St7ExportImage(self.uID, str(fn).encode(), image_type.value, width, height))

    def St7SetPlateResultDisplay_None(self):
        # TODO!
        pass

    def St7SetPlateResultDisplay(self, plate_result_display: arrays.PlateResultDisplay):
        ints_arr = plate_result_display.get_single_sub_array_instance_of_type(
            ctypes.c_long
        ).to_st7_array()

        chk(St7API.St7SetPlateResultDisplay(self.uID, ints_arr))

    def St7SetWindowResultCase(self, case_num: int):
        chk(St7API.St7SetWindowResultCase(self.uID, case_num))

    def St7RedrawModel(self, rescale: bool):
        chk(St7API.St7RedrawModel(self.uID, rescale))

    def St7SetDisplacementScale(self, disp_scale: float, scale_type: const.ScaleType):
        chk(St7API.St7SetDisplacementScale(self.uID, disp_scale, scale_type.value))

    def St7GetEntityContourSettingsStyle(self, entity: const.Entity) -> arrays.ContourSettingsStyle:
        ints = arrays.ContourSettingsStyle.get_single_sub_array_of_type(ctypes.c_long)
        ints_arr = ints.make_empty_array()

        chk(St7API.St7GetEntityContourSettingsStyle(self.uID, entity.value, ints_arr))

        ints_instance = ints.instance_from_st7_array(ints_arr)
        return arrays.ContourSettingsStyle.instance_from_sub_array_instances(ints_instance)

    def St7SetEntityContourSettingsStyle(
        self, entity: const.Entity, contour_settings_style: arrays.ContourSettingsStyle
    ):
        ints_arr = contour_settings_style.get_single_sub_array_instance_of_type(
            ctypes.c_long
        ).to_st7_array()
        chk(St7API.St7SetEntityContourSettingsStyle(self.uID, entity.value, ints_arr))

    def St7GetEntityContourSettingsLimits(
        self, entity: const.Entity
    ) -> arrays.ContourSettingsLimit:
        ints = arrays.ContourSettingsLimit.get_single_sub_array_of_type(ctypes.c_long)
        doubles = arrays.ContourSettingsLimit.get_single_sub_array_of_type(ctypes.c_double)

        ints_arr = ints.make_empty_array()
        doubles_arr = doubles.make_empty_array()

        chk(St7API.St7GetEntityContourSettingsLimits(self.uID, entity.value, ints_arr, doubles_arr))

        ints_instance = ints.instance_from_st7_array(ints_arr)
        doubles_instance = doubles.instance_from_st7_array(doubles_arr)

        contour_settings_limit = arrays.ContourSettingsLimit.instance_from_sub_array_instances(
            ints_instance, doubles_instance
        )

        return contour_settings_limit

    def St7SetEntityContourSettingsLimits(
        self, entity: const.Entity, contour_settings_limit: arrays.ContourSettingsLimit
    ):

        ints_arr = contour_settings_limit.get_single_sub_array_instance_of_type(
            ctypes.c_long
        ).to_st7_array()
        doubles_arr = contour_settings_limit.get_single_sub_array_instance_of_type(
            ctypes.c_double
        ).to_st7_array()

        chk(St7API.St7SetEntityContourSettingsLimits(self.uID, entity.value, ints_arr, doubles_arr))


def _DummyClassFactory(name, BaseClass):
    """Utility function to make a class with no-op methods for everything, but the same signature."""

    def make_no_op_function(func_returns_self: bool) -> typing.Callable:
        # Factory to make
        if func_returns_self:

            def f(self, *args, **kwargs):
                return self

        else:

            def f(*args, **kwargs):
                pass

        return f

    # Build a new dictionary of no-op functions for all the user-defined things in the base class.
    attribute_dict = {}
    for attr_name in dir(BaseClass):
        attr = getattr(BaseClass, attr_name)

        is_dunder = attr_name.startswith("__")
        is_callable = callable(attr)
        if not is_dunder:
            if is_callable:
                # For methods
                attribute_dict[attr_name] = make_no_op_function(func_returns_self=False)

            else:
                # For other attributes
                attribute_dict[attr_name] = None

    # Add the special cases.
    attribute_dict["__init__"] = make_no_op_function(func_returns_self=False)
    attribute_dict["__enter__"] = make_no_op_function(func_returns_self=True)
    attribute_dict["__exit__"] = make_no_op_function(func_returns_self=False)

    # The rest can be inherited.
    NewClass = type(name, (BaseClass,), attribute_dict)
    return NewClass


St7ModelWindowDummy = _DummyClassFactory("St7ModelWindowDummy", St7ModelWindow)
