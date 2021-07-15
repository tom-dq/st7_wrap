from st7_wrap import const
from st7_wrap import exc
from st7_wrap import st7


with st7.St7NewModel(r"c:\temp\Model.st7") as st7_model:

    # No error expected
    st7_model.St7SetNodeXYZ(1, [1.0, 1.0, 0.0])

    # Non-zero return codes are translated into exceptions to manage in the usual Python way
    try:
        missing_node = st7_model.St7GetNodeXYZ(999)

    except exc.ERR7_ExceededTotal:
        print("Didn't find that node sorry.")

    # To catch all Strand7 exceptions (ERR7_... or SE_...), use St7BaseException
    try:
        no_plate = st7_model.St7GetElementConnection(const.Entity.tyPLATE, 12345)

    except exc.St7BaseException:
        print("Some non-zero return code from a Strand7 function.")
