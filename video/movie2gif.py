from moviepy.editor import *

#  ---- Parameters ----

input_file = "~/resource/input.mov"
output_file = "~/resource/output.gif"
t_start = (0, 11.00)
t_end = (0, 12.00)
resize = 0.2

# ---------------------


clip = VideoFileClip(input_file).subclip(t_start, t_end).resize(resize)

clip.write_gif(output_file)
