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
