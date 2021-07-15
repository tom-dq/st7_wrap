import St7API

from st7_wrap import arrays
from st7_wrap import const
from st7_wrap import st7


# This should be a model with plates in it which is ready to solve.
with st7.St7OpenFile(r"c:\temp\ExistingModel.st7") as st7_model:

    # Run the solver
    st7_model.St7RunSolver(
        const.SolverType.stLinearStatic, const.SolverMode.smBackgroundRun, wait=True
    )

    # Create a model window to save images of the model or results.
    with st7_model.St7CreateModelWindow() as model_window:
        with st7_model.open_results(r"c:\temp\ExistingModel.LSA") as st7_results:

            model_window.St7SetWindowResultCase(case_num=1)

            # Set the model window contour to vM stress
            PLATE_STRESS_COMBINED_VM_GUI_IDX = 4
            plate_result_display = arrays.PlateResultDisplay(
                ipResultType=St7API.rtAsContour,
                ipResultQuantity=St7API.rqPlateStressC,
                ipResultSystem=St7API.stPlateCombined,
                ipResultComponent=PLATE_STRESS_COMBINED_VM_GUI_IDX,
                ipResultSurface=St7API.psPlateMidPlane,
            )

            model_window.St7SetPlateResultDisplay(plate_result_display)
            model_window.St7SetDisplacementScale(5.0, const.ScaleType.dsAbsolute)
            model_window.St7RedrawModel(True)

            model_window.St7ExportImage(
                r"c:\temp\St7Results.png", const.ImageType.itPNG, 1600, 1200
            )
