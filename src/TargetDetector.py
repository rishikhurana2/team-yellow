import cv2
import numpy as np

class TargetDetector:
	def findImg(self, image):
		global img
		img = image
		global hsv_img
		hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	def threshed(self):
		global img
		global hsv_img
		THRESHOLD_MIN = np.array([50,0,0],np.uint8)
		THRESHOLD_MAX = np.array([60,50,255],np.uint8)
		frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)
		return frame_threshed

# Yo Rishi, you need to completely change this, you didn't to contours in this
# Add these functions in during the session, please.
#

# TargetDetect() = inputs the camera frame and processes it, should output a single contour and if there aren't any contours make the "found" boolean 0
# getFound() = if a target is found, 0 or 1 output
#
