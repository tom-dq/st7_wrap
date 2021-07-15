import St7API

from st7_wrap import const
from st7_wrap import st7

# This should be a model with plates in it which is ready to solve.
with st7.St7ExistingModel(r"c:\temp\ExistingModel.st7") as st7_model:

    # Run the solver
    st7_model.St7RunSolver(
        const.SolverType.stLinearStatic, const.SolverMode.smBackgroundRun, wait=True
    )

    # Context manager for St7OpenResultFile on entry and St7CloseResultFile at the end.
    with st7_model.open_results(r"c:\temp\ExistingModel.LSA") as st7_results:

        case_num = 1
        layer = 0

        # Display node results
        for node_num in st7_model.entity_numbers(const.Entity.tyNODE):
            node_result = st7_results.St7GetNodeResult(
                const.NodeResultType.rtNodeDisp, node_num, case_num
            )
            print(f"Node {node_num}: {node_result.results[0:3]}")

        # Display plate results
        for plate_num in st7_model.entity_numbers(const.Entity.tyPLATE):
            plate_result = st7_results.St7GetPlateResultArray(
                const.PlateResultType.rtPlateStress,
                const.PlateResultSubType.stPlateCombined,
                plate_num,
                case_num,
                const.SampleLocation.spGaussPoints,
                const.PlateSurface.psPlateMidPlane,
                layer,
            )

            # Select out the Gauss point vM Stress
            gauss_points = range(plate_result.num_points)
            gp_vm_res = [
                plate_result.results[iGP * plate_result.num_cols + St7API.ipPlateCombVonMises]
                for iGP in gauss_points
            ]
            print(f"Plate {plate_num} vM Stress at Gauss Points: {gp_vm_res}")
