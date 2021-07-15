from st7_wrap import const
from st7_wrap import st7


# Context manager handles St7OpenFile or St7NewFile, then St7CloseFile at the end.
with st7.St7NewFile(r"c:\temp\NewModel.st7") as st7_model:

    # Make some nodes - Vector3 type has some conveniences, or just use a list or tuple.
    st7_model.St7SetNodeXYZ(1, st7.Vector3(1.0, 1.0, 0.0))
    st7_model.St7SetNodeXYZ(2, (3.0, 1.5, 0.0))
    st7_model.St7SetNodeXYZ(3, [2.0, 3.0, 0.0])

    # Make a plate
    st7_model.St7SetElementConnection(
        const.Entity.tyPLATE, elem_num=1, prop_num=1, connection=[1, 2, 3]
    )

    st7_model.St7SaveFile()
