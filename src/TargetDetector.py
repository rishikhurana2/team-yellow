'''Target Detector

Identifies if target is in the input image or not.
'''

import cv2
import numpy as np
import math

class TargetDetector:

	def threshold(self, image):
		'''Thresholds an input image'''

		global img
		img = image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		THRESHOLD_MIN = np.array([100,0,100],np.uint8)
		THRESHOLD_MAX = np.array([255,255,255],np.uint8)
		img = cv2.inRange(image, THRESHOLD_MIN, THRESHOLD_MAX)
		cv2.imshow("Threshed Image", img)
		return img

		
	def contour(self, image):
		'''Finds where the target is located.

		Finds contours in the thresholded image then find the most accurate contour through a series of filters.
		Filters based on numer of corners, size of contour, and corner angles.
		'''

		maxX = 0
		maxY = 0
		minX = 10000
		minY = 10000

		self.found = False
		count = -1

		images, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		for cont in contours:
			count += 1

			approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
			area = cv2.contourArea(approx)
			if len(approx) == 4 and area > 300:
				return approx
				for i in approx:
					if i[0][0] > maxX:
						maxX = i[0][0]
					if i[0][0] < minX:
						minX = i[0][0]
					if i[0][1] > maxY:
						maxY = i[0][1]
					if i[0][1] < minY:
						minY = i[0][1]
				width = math.sqrt(math.abs((i[0]-i[0])**2 + math.abs((i[0]-i[0])**2))
				height = math.sqrt(math.abs((i[0]-i[0])**2 + abs((i[1]-i[1])**2))
				if (width/height == 4 or width/height == 5):
					self.found = True
        def getFound(self):
        #Returns if the target is found or not'''

                return self.found


