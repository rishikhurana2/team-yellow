import cv2
import numpy as np

class TargetDetector:
	def threshold(self, image):
		global img
		img = image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		
		THRESHOLD_MIN = np.array([100,0,100],np.uint8)
		THRESHOLD_MAX = np.array([255,255,255],np.uint8)
		img = cv2.inRange(image, THRESHOLD_MIN, THRESHOLD_MAX)
		cv2.imshow("Threshed", img)
		return img
		
	def contour(self, image):
		maxX = 0
		maxY = 0
		minX = 10000
		minY = 10000
		x = 1
		self.found = False
		#cv2.imshow("Threshed", frame_threshed)
		count = -1

		images, contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(Cimg, contours, count, (255,255,255), 2)
		#cv2.imshow("Contour Image", Cimg)
		
		for cont in contours:
			count += 1
			
			approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
			area = cv2.contourArea(approx)
			if len(approx) == 4 and area > 300:
				cv2.drawContours(image, contours, count, (255,255,255), 10)
				self.found = True
				return approx
				if i[0][0] > maxX:
					maxX = i[0][0]
				if i[0][0] < minX:
					minX = i[0][0]
				if i[0][1] > maxY:
					maxY = i[0][1]
				if i[0][1] < minY:
					minY = i[0][1]
				width = maxX - minX
				height = maxY -minY
				return self.width
				return self. height
				print("width: " + width + "height: " + height)
		cv2.imshow("Contour Image", image)
	def getFound(self):
			return self.found
