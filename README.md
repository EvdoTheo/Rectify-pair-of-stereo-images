# Rectify-pair-of-stereo-images
During my diploma dissertaion research i had to do receive a pair of rectified stereo images in order to post process them.
Rectifying images includes some pre process steps in order to retrieve information about the intrinsic and extrinsic camera parameters.

-First step: For the Calibration Procedure make use of:
  1) cv2.stereoCalibrate 
  2) cv2.stereoRectify

-Once you retrieve the camera parameters ( distortion matrix, camera matrix, rectification matrix), the next step is the rectification process:
  1) cv2.initUndistortRectifyMap
  2) cv2.remap


