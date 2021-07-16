Here's what I do to get set up for local development:

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

 - Crop an animated gif from a recording

`ffmpeg -i demo_full_2.mp4 -vf "crop=800:230:300:75,fps=24,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output2.gif`