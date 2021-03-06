# st7_wrap

An opinionated wrapper around the Strand7 / Straus7 API. Not affiliated with Strand7 Pty Ltd.


## Background

Over the years I've used the Strand7 API on a number of projects, and sometimes the first step was building a quick-and-dirty wrapper. Now I hope I won't need to make a similar one next time a project comes along, and if you can make use of it, all the better.


## Installation

 - Ensure you've installed [Strand7](http://www.strand7.com/) Release 3.1.1.
 - Use Python 3.7+
 - Make sure the official Strand7 API is installed and running (contact [Strand7 Support](https://www.strand7.com/html/aboutsupport.htm) if this is not the case). So you should be able to do this in the Python REPL where ever you want
 to use `st7_wrap`:

 ```python
 >>> import St7API
 >>> St7API.St7Init()
 0
 ```

- Then you can install it the usual way:
```
pip install st7_wrap
```

## Examples

Note that this is very far from feature complete - I wouldn't recommend depending on this for long-lived or production work.

Feedback is most welcome via GitHub issues.

### Creating a new model

```python
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

```

### Handling errors

If any St7API function is called through `st7_wrap` and it returns a non-zero error code, the
error code is converted into a Python exception to handle in the conventional way.

If you don't
care what the particular error is and want to catch everything non-zero, they all inherit from
`St7BaseException`.


```python
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

```

Output:
```
Couldn't get node 999.

Error from St7GetElementConnection(const.Entity.tyPLATE, -10):     
ERR7_InvalidEntityNumber: The specified entity number is not valid.
```

### Change a plate property
Python `dataclasses` are used for Strand7 arrays where you set things using `ip...` index
position constants. These can be found in `st7_wrap.arrays` and give some niceties like
autocompletion.

![Autocomplete in arrays](images/array_autocomplete.GIF)

*This interface in particular is incomplete and might change in the future*

```python
import dataclasses

from st7_wrap import st7
from st7_wrap import arrays

PLATE_PROP_NUM = 1

# This is a model with a plate property in it.
with st7.St7OpenFile(r"c:\temp\ExistingModel.st7") as st7_model:

    # Set the plate modulus to something specific - any unset argument will be zero.
    new_plate_prop = arrays.PlateIsotropicMaterial(ipPlateIsoModulus=200e3, ipPlateIsoPoisson=0.3)
    st7_model.St7SetPlateIsotropicMaterial(PLATE_PROP_NUM, new_plate_prop)

    # To change some values without overwriting the others with zero, get the existing values first
    existing_plate_prop = st7_model.St7GetPlateIsotropicMaterial(PLATE_PROP_NUM)
    updated_plate_prop = dataclasses.replace(existing_plate_prop, ipPlateIsoModulus=220e3)
    st7_model.St7SetPlateIsotropicMaterial(PLATE_PROP_NUM, updated_plate_prop)

    st7_model.St7SaveFile()
```

### Running the solver and extracting results

```python
import St7API

from st7_wrap import const
from st7_wrap import st7

# This should be a model with plates in it which is ready to solve.
with st7.St7OpenFile(r"c:\temp\ExistingModel.st7") as st7_model:

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

```

Output:
```
...
Node 254: (0.004691353609810177, -0.01586862433334294, 0.0)
Node 255: (0.005981213780284651, -0.016060926198869913, 0.0)
Node 256: (0.0075936501484970866, -0.016145524500278237, 0.0)
Plate 1 vM Stress at Gauss Points: [5569.576626668302, 11700.175314227161, 4844.353537104418, 11462.512122246826]
Plate 2 vM Stress at Gauss Points: [13893.919745642319, 10053.730619615291, 13953.137294350929, 10143.769927789555]
Plate 3 vM Stress at Gauss Points: [8335.799952936248, 7027.347709115354, 8334.841407078804, 7034.758429109735]
Plate 4 vM Stress at Gauss Points: [6271.495334295235, 5522.062758482633, 6266.697307849912, 5517.164372917556]
Plate 5 vM Stress at Gauss Points: [5017.202557134458, 4347.615893517061, 5015.150140264017, 4345.975844187045]
...
```

### Model Window

```python
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
```

Then if you open up `c:\temp\St7Results.png` you will have an image of the results:
![Autocomplete in arrays](images/St7Results.png)


## Acknowledgments

This module has been created as a part of my PhD, with funding support from 
the Australian Reseach Council grant *TODO grant number*. Additional thanks to Strand7 Pty Ltd for
the use of their finite element analysis software during the PhD.

If you're using this for your own research and feel so inclined, please cite the
publication from which it was extracted, *TODO plasticity band paper*.

