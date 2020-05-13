from moviepy.editor import *

# ----- Parameters ---------

# files
inputFilePath = './resource/input.mp4'
outputFilePath = './resource/output.mp4'

# crop range
upperLeftPoint = [0,0]
lowerRightPoint = [100, 100]

# fps
outputFps = 30

# --------------------------

xs = upperLeftPoint[0]
ys = upperLeftPoint[1]
xe = lowerRightPoint[0]
ye = lowerRightPoint[0]

video = VideoFileClip(inputFilePath).crop(x1=xs, y1=ys, x2=xe, y2=ye)
video.write_videofile(outputFilePath, fps=outputFps)