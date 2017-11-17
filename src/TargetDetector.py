import cv2
import numpy as np
from VideoDevice import VideoDevice

class TargetDetector:
	def TargetDetect(self, image):
		global hsv_img
		global Cimg
		Cimg = image
		hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		cv2.imshow("HSV Image", hsv_img)
		THRESHOLD_MIN = np.array([100,0,100],np.uint8)
		THRESHOLD_MAX = np.array([255,255,255],np.uint8)
		frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)
		cv2.imshow("Threshed", frame_threshed)
		count = -1
		global images
		global contours
		global hierarchy
		images, contours, hierarchy = cv2.findContours(frame_threshed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(Cimg,contours,count,(255,255,255),2)
		cv2.imshow("Contour Image", Cimg)
	def getFound(self):
		global contours
		if contours == True:
			return True
		else:
			return false  #is this right?
# TargetDetect() = inputs the camera frame and processes it, should output a single contour and if there aren't any contours make the "found" boolean 0
# getFound() = if a target is found, 0 or 1 output

