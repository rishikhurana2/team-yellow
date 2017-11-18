import cv2
import math

class Target:
	def __init__(self, approx):
		points = [0 for y in xrange(4)]
		
		for x in xrange(4):
			points[x] = approx[x]
		
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

		self.center = [0, 0]
		self.width = 0
		self.height = 0
		
		# H = 0, S = 1, V = 2
		self.targetType = -1
		for x in range(4):
			self.center[0] += points[x][0]
			self.center[1] += points[x][1]

			if x == 3:
				self.center[0] /= 4
				self.center[1] /= 4

		self.width = int(math.sqrt(((points[yValue[0]][1] - points[yValue[1]][1])**2) + ((points[yValue[0]][0] - points[yValue[1]][0])**2)))
		self.height = int(math.sqrt(((points[xValue[0]][1] - points[xValue[1]][1])**2) + ((points[xValue[0]][0] - points[xValue[1]][0])**2)))

		if width > height and abs([yValue[0]][1] - points[yValue[1]][1]) < width * 0.1:
			self.targetType = 0
		if height > width and abs([xValue[0]][0] - points[xValue[1]][0]) < height * 0.1:
			self.targetType = 2
		else:
			self.targetType = 3

	def getType(self):
		return self.targetType

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getCenter(self):
		return self.center
		
