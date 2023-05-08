from moviepy.editor import *

# ----- Parameters ---------

# files
input_file_name = "./resource/input.mp4"
output_file_name = "./resource/output.mp4"

# crop range
upper_left_point = [0, 0]
lower_right_point = [100, 100]

# fps
output_fps = 30

# --------------------------

xs = upper_left_point[0]
ys = upper_left_point[1]
xe = lower_right_point[0]
ye = lower_right_point[0]

video = VideoFileClip(input_file_name).crop(x1=xs, y1=ys, x2=xe, y2=ye)
video.write_videofile(output_file_name, fps=output_fps)
