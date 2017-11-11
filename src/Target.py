import cv2
import math

class Target:
	def __init__(self, contour):
		# Initialize array of size 4x2 to contain 4 points with (x,y) tuples
		points = [[0 for y in range(4)] for x in range(2)]

		# Draw a rotated bounding box that minimizes area outside of rectangle		
		rect = cv2.boundingRect(contour)
		
		# May be errors here, Rishi please check if it works
		#		
		# Take out the 4 points of the rectangle
		corners = cv2.boxPoints(rect):
		
		# Place all 8 points into the initialized array
		count = 0
		for point in corners:
			points[count][0] = point.pt[0]
			points[count][1] = point.py[1]
		#
		#
		#

		# Find which ones are "pairs"
		xValue = []
		yValue = []
		for y in range(4):
			for x in range(len(xValue) + 1):
				if x == len(xValue):
					xValue.insert(y, x)

				if points[xValue[x]][0] < points[y][0]:
					xValue.insert(y, x)

			for x in range(len(yValue) + 1):
				if x == len(yValue):
					yValue.insert(y, x)

				if points[yValue[x]][1] < points[y][1]:
					yValue.insert(y, x)

		center = [0, 0]
		width = 0
		height = 0
		# H = 0, S = 1, V = 2
		targetType = -1
		for x in range(4):
			center[0] += points[x][0]
			center[1] += points[x][1]

			if x == 3:
				center[0] /= 4
				center[1] /= 4

		width = int(math.sqrt(((points[yValue[0]][1] - points[yValue[1]][1])**2) + ((points[yValue[0]][0] - points[yValue[1]][0])**2)))
		height = int(math.sqrt(((points[xValue[0]][1] - points[xValue[1]][1])**2) + ((points[xValue[0]][0] - points[xValue[1]][0])**2)))

		if width > height and abs(yValue[0]][1] - points[yValue[1]][1]) < width * 0.1:
			targetType = 0
		if height > width and abs(xValue[0]][0] - points[xValue[1]][0]) < height * 0.1:
			targetType = 2
		else:
			targetType = 3

	def getType(self):
		return self.targetType

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getCenter(self):
		return self.center
		
