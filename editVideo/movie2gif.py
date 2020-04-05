from moviepy.editor import *

#  ---- Parameters ----

inputFile = 'input.mov'
outputFile = 'output.gif'
startT = (0,10.00)
endT = (0,10.80)
resize = 0.1

# ---------------------


clip = (VideoFileClip(inputFile)
  .subclip(startT, endT)
  .resize(resize))

clip.write_gif(outputFile)