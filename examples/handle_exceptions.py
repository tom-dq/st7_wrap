from st7_wrap import const
from st7_wrap import exc
from st7_wrap import st7


with st7.St7NewFile(r"c:\temp\Model.st7") as st7_model:

    # No error expected
    st7_model.St7SetNodeXYZ(1, [1.0, 1.0, 0.0])

    # Non-zero return codes are translated into exceptions to manage in the usual Python way
    try:
        missing_node = st7_model.St7GetNodeXYZ(999)

    except exc.ERR7_ExceededTotal:
        print("Couldn't get node 999.\n")

    # To catch all Strand7 exceptions (ERR7_... or SE_...), use St7BaseException
    try:
        no_plate = st7_model.St7GetElementConnection(const.Entity.tyPLATE, -10)

    except exc.St7BaseException as e:
        print("Error from St7GetElementConnection(const.Entity.tyPLATE, -10):")
        print(e)
