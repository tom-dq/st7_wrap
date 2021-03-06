## Local Dev

Here's what I do to get set up for local development

 - Clone the repository locally.
 - Make a vitrual env
 
 `PS C:\SomeDirectory\st7_wrap>py -m venv venv --upgrade-deps --prompt st7_wrap`
 - Activate it the usual way

 ``` 
 > .\venv\Scripts\activate.ps1
(st7_wrap) PS C:\SomeDirectory\st7_wrap> 
 ```

 - Install the development dependencies

`pip install -r .\requirements_dev.txt`

 ## Updating to a new version of the Strand7 API.

 1. Copy the new `ST7API.py` to all the places it needs to be (`build`, `examples`, `src\st7_wrap`).
 1. Regenerate constants and exceptions by running `build\_constants_generate.py` and `build\_exceptions_generate`.
 1. Format updated code with Black. Note to myself - in my VSCode this is Shift-Alt-F to reformat.
 1. Compare the changes and commit them if all good.
 1. Update `README.md` with the new version

## Creating a package
 1. Bump the version number in `setup.cfg`
 1. Build with `py -m build`
 1. Upload to PyPI with `py -m twine upload dist/st7_wrap-0.0.2*` (or whatever the latest version is)

 ## Crop an animated gif from a recording

`ffmpeg -i demo_full_2.mp4 -vf "crop=800:230:300:75,fps=24,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output2.gif`

