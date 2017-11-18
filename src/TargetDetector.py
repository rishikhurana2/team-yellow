import cv2
import numpy as np

class TargetDetector:
	def threshold(self, image):
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		#cv2.imshow("HSV Image", hsv_img)
		
		THRESHOLD_MIN = np.array([100,0,100],np.uint8)
		THRESHOLD_MAX = np.array([255,255,255],np.uint8)
		
		image = cv2.inRange(image, THRESHOLD_MIN, THRESHOLD_MAX)
		
		return image
		
	def contour(self, image)
		self.found = False
		#cv2.imshow("Threshed", frame_threshed)
		count = -1

		images, contours, hierarchy = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(Cimg, contours, count, (255,255,255), 2)
		#cv2.imshow("Contour Image", Cimg)
		
		for cont in contours:
			count += 1
			
			approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
			area = cv2.contourArea(approx)
			if len(approx) == 4 and area > 300:
				self.found = True
				return approx
		
	def getFound(self):
			return self.found
