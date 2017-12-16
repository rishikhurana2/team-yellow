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
		THRESHOLD_MIN = np.array([100,51,175],np.uint8)
		THRESHOLD_MAX = np.array([150,207,255],np.uint8)
		img = cv2.inRange(image, THRESHOLD_MIN, THRESHOLD_MAX)
		cv2.imshow("Threshed Image", img)
		return img

		
	def contour(self, image):
		'''Finds where the target is located.

		Finds contours in the thresholded image then find the most accurate contour through a series of filters.
		Filters based on numer of corners, size of contour, and corner angles.
		'''

		self.found = False
		count = -1

		images, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		for cont in contours:
			count += 1
			approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
			area = cv2.contourArea(approx)
			if len(approx) == 4 and area > 300:

				upperPoints = [[0 for y in range(2)] for x in range(2)]
				rightPoints = [[0 for y in range(2)] for x in range(2)]

				for i in approx:
					if i[0][0] > rightPoints[0][0]:
						rightPoints[1][0] = rightPoints[0][0]
						rightPoints[1][1] = rightPoints[0][1]

						rightPoints[0][0] = i[0][0]
						rightPoints[0][1] = i[0][1]

					elif i[0][0] > rightPoints[1][0]:
						rightPoints[1][0] = i[0][0]
						rightPoints[1][1] = i[0][1]

					if i[0][1] > upperPoints[0][1]:
						upperPoints[1][0] = upperPoints[0][0]
						upperPoints[1][1] = upperPoints[0][1]

						upperPoints[0][0] = i[0][0]
						upperPoints[0][1] = i[0][1]

					elif i[0][1] > upperPoints[1][1]:
						upperPoints[1][0] = i[0][0]
						upperPoints[1][1] = i[0][1]

				width = int(math.sqrt(((upperPoints[0][0]-upperPoints[1][0])**2) + ((upperPoints[0][1] - upperPoints[1][1])**2)))
				height = int(math.sqrt(((rightPoints[0][0]-rightPoints[1][0])**2) + ((rightPoints[0][1] - rightPoints[1][1])**2)))
				print(width)
				print(height)
				if (width/height > 3.5 and width/height < 4.5):
					self.found = True
				elif (height/width > 0.20 and height/width < 0.30):
					self.found = True

				return approx

	def getFound(self):
	#Returns if the target is found or not'''
		return self.found


