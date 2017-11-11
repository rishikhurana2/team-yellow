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
