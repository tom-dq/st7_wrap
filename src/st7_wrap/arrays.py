"""Interface which uses dataclasses to get/set arguments to Strand7 function, 
where those functions use arrays of arguments with ipXXX indexed arrays"""


import collections
import ctypes
import dataclasses
import typing

import St7API


_ARRAY_NAME = "array_name"


_T_ctypes_type = typing.Union[typing.Type[ctypes.c_long], typing.Type[ctypes.c_double]]


class _InternalSubArrayDefinition(typing.NamedTuple):
    """Represents, for example, the "Integers" argument of St7SetEntityContourSettingsLimits -
    how many values there are in there, what type they are, etc."""

    elem_type: _T_ctypes_type  # e.g., ctypes.c_long, ctypes.c_double  (not an instance like ctypes.c_long(34)... )
    fields: typing.List[dataclasses.Field]
    array_name_override: str

    @property
    def array_name(self) -> str:
        if self.array_name_override:
            return self.array_name_override

        lookups = {
            ctypes.c_long: "Integers",
            ctypes.c_double: "Doubles",
        }

        return lookups[self.elem_type]

    @property
    def array_length(self) -> int:
        # Have a buffer on there in case...
        return 10 + max(getattr(St7API, field.name) for field in self.fields)

    def make_empty_array(self):
        array = (self.elem_type * self.array_length)()
        return array

    def instance_from_st7_array(self, ints_or_floats) -> "_InternalSubArrayInstance":
        values = {}

        for field in self.fields:
            idx = getattr(St7API, field.name)
            values[field.name] = field.type(ints_or_floats[idx])  # Convert to int if it's a bool

        return _InternalSubArrayInstance(array_def=self, values=values)


class _InternalSubArrayInstance(typing.NamedTuple):
    """Represents an instance of, say, the "Integers" argument of St7SetEntityContourSettingsLimits
    populated with values"""

    array_def: _InternalSubArrayDefinition
    values: typing.Dict[str, typing.Union[bool, int, float]]

    def to_st7_array(self):
        working_array = self.array_def.make_empty_array()

        for key, val in self.values.items():
            idx = getattr(St7API, key)
            working_array[idx] = val

        return working_array


@dataclasses.dataclass
class _St7ArrayBase:
    """All those arrays of integers, etc can inherit from this to get convenience conversion functions."""

    # TODO - future plan for functions in which there are multiple arrays of the same type,
    #   like "St7GetBeamPropertyData" with two Doubles arrays:
    #   Support custom field creation like this
    #   ipAREA : float = field(metadata={"array_name": "SectionData"})
    #   ipModulus : float = field(metadata={"array_name": "MaterialData"})

    # Also TODO: support stuff like connection arrays? Or things where there is no ipAAA constant?

    # Another TODO - it would be good to be able to convert to and from enums where they appear in an integer array.

    @classmethod
    def get_sub_arrays(cls) -> typing.Iterable[_InternalSubArrayDefinition]:
        def sub_array_key(field: dataclasses.Field):

            if field.type in {int, bool}:
                c_type = ctypes.c_long

            elif field.type == float:
                c_type = ctypes.c_double

            else:
                raise ValueError(field)

            array_name_override = field.metadata.get(_ARRAY_NAME, "")

            return c_type, array_name_override

        # Collect the sub-array keys
        sub_array_list = collections.defaultdict(list)

        for field in dataclasses.fields(cls):
            sub_array_list[sub_array_key(field)].append(field)

        for (c_type, array_name_override), fields in sub_array_list.items():
            yield _InternalSubArrayDefinition(
                elem_type=c_type, fields=fields, array_name_override=array_name_override
            )

    def get_sub_array_instances(self) -> typing.Iterable[_InternalSubArrayInstance]:
        instance_values = dataclasses.asdict(self)

        for sub_array_def in self.get_sub_arrays():
            this_subarray_instance_values = {}
            for field in sub_array_def.fields:
                key = field.name
                this_subarray_instance_values[key] = instance_values.pop(key)

            yield _InternalSubArrayInstance(
                array_def=sub_array_def, values=this_subarray_instance_values
            )

        if instance_values:
            raise ValueError(f"did not find a sub-array for the following: {instance_values}")

    @classmethod
    def get_single_sub_array_of_type(
        cls, target_type: _T_ctypes_type
    ) -> _InternalSubArrayDefinition:

        all_matches = [
            sub_array for sub_array in cls.get_sub_arrays() if sub_array.elem_type == target_type
        ]

        if len(all_matches) == 1:
            return all_matches.pop()

        raise ValueError(
            f"Expected one array of type {target_type} - got {len(all_matches)}: {all_matches}"
        )

    def get_single_sub_array_instance_of_type(
        self, target_type: _T_ctypes_type
    ) -> _InternalSubArrayInstance:
        all_matches = [
            sub_array_inst
            for sub_array_inst in self.get_sub_array_instances()
            if sub_array_inst.array_def.elem_type == target_type
        ]

        if len(all_matches) == 1:
            return all_matches.pop()

        raise ValueError(
            f"Expected one array instance of type {target_type} - got {len(all_matches)}: {all_matches}"
        )

    @classmethod
    def instance_from_sub_array_instances(
        cls, *sub_array_instances: _InternalSubArrayInstance
    ) -> "_St7ArrayBase":
        working_dict = {}
        for sub_array_instance in sub_array_instances:
            working_dict.update(sub_array_instance.values)

        return cls(**working_dict)

    @classmethod
    def from_st7_array(cls, ints_or_floats):
        working_dict = {}

        for field in dataclasses.fields(cls):
            idx = getattr(St7API, field.name)
            working_dict[field.name] = field.type(ints_or_floats[idx])  # Convert to int

        return cls(**working_dict)

    def to_st7_array(self) -> ctypes.Array:
        name_to_idx = {
            field.name: getattr(St7API, field.name) for field in dataclasses.fields(self)
        }

        array = self.make_empty_array()

        for field, value in dataclasses.asdict(self).items():
            idx = name_to_idx[field]
            array[idx] = value

        return array

    @classmethod
    def get_array_length(cls) -> int:
        # Have a buffer on there in case...
        return 10 + max(getattr(St7API, field.name) for field in dataclasses.fields(cls))

    @classmethod
    def get_array_element_type(cls):
        """Returns ctypes element type"""
        all_types = {field.type for field in dataclasses.fields(cls)}

        if all_types <= {int, bool}:
            return ctypes.c_long

        elif all_types == {float}:
            return ctypes.c_double

        else:
            raise ValueError(all_types)


@dataclasses.dataclass
class ContourSettingsStyle(_St7ArrayBase):
    ipContourStyle: int = 0
    ipReverse: bool = False
    ipSeparator: bool = False
    ipBand1Colour: int = 0
    ipBand2Colour: int = 0
    ipSeparatorColour: int = 0
    ipLineBackColour: int = 0
    ipMonoColour: int = 0
    ipMinColour: int = 0
    ipMaxColour: int = 0
    ipLimitMin: bool = False
    ipLimitMax: bool = False


@dataclasses.dataclass
class ContourSettingsLimit(_St7ArrayBase):
    ipContourLimit: int = 0
    ipContourMode: int = 0
    ipNumContours: int = 0
    ipSetMinLimit: bool = False
    ipSetMaxLimit: bool = False

    ipMinLimit: float = 0.0
    ipMaxLimit: float = 0.0


@dataclasses.dataclass
class PlateIsotropicMaterial(_St7ArrayBase):
    ipPlateIsoModulus: float = 0.0
    ipPlateIsoPoisson: float = 0.0
    ipPlateIsoDensity: float = 0.0
    ipPlateIsoAlpha: float = 0.0
    ipPlateIsoViscosity: float = 0.0
    ipPlateIsoDampingRatio: float = 0.0
    ipPlateIsoConductivity: float = 0.0
    ipPlateIsoSpecificHeat: float = 0.0


@dataclasses.dataclass
class PlateResultDisplay(_St7ArrayBase):
    ipResultType: int = 0
    ipResultQuantity: int = 0
    ipResultSystem: int = 0
    ipResultComponent: int = 0
    ipResultSurface: int = 0
    ipVectorStyle: int = 0
    ipReferenceNode: int = 0
    ipAbsoluteValue: int = 0
    ipVector1: int = 0
    ipVector2: int = 0
    ipVector3: int = 0
    ipVector4: int = 0
    ipVector5: int = 0
    ipVector6: int = 0
