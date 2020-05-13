from moviepy.editor import *

#  ---- Parameters ----

inputFile = '~/resource/input.mov'
outputFile = '~/resource/output.gif'
startT = (0,11.00)
endT = (0,12.00)
resize = 0.2

# ---------------------


clip = (VideoFileClip(inputFile)
  .subclip(startT, endT)
  .resize(resize))

clip.write_gif(outputFile)
