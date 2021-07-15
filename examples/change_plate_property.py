import dataclasses

from st7_wrap import st7

PLATE_PROP_NUM = 1

# This is a model with a plate property in it.
with st7.St7ExistingModel(r"c:\temp\ExistingModel.st7") as st7_model:

    # Set the plate modulus to something specific
    plate_iso_prop = st7_model.St7GetPlateIsotropicMaterial(PLATE_PROP_NUM)
    new_plate_iso_prop = dataclasses.replace(plate_iso_prop, ipPlateIsoModulus=123456.789)
    st7_model.St7SetPlateIsotropicMaterial(PLATE_PROP_NUM, new_plate_iso_prop)

    st7_model.St7SaveFile()
