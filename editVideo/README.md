# editVideo
Utilities about video editing

## [cropVideo](cropVideo.py)
Spatially crop video

### Parameters
- `inputFilePath`: input file name
- `outputFilePath`: output file name
- crop range
  - `upperLeftPoint` 
  - `lowerRightPoint`
- `outputFps`: fps

## [movie2gif](movie2gif.py)
Convert movie file to gif
### Parameters
- `inputFile` = 'input.mov'
- `outputFile` = 'output.gif'
- Crop sequentially (format: (minutes,seconds.milliseconds))
  - `startT`
  - `endT`
- `resize`: resize the original file (0 - 1)