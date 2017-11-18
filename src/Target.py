import cv2
import math

class Target:
	def __init__(self, approx):
		minX = temp[0][0][0]
        maxX = temp[0][0][0]
        minY = temp[0][0][1]
        maxY = temp[0][0][1]
		
		upperPoints = [[0 for y in range(2)] for x in range(0)]
		rightPoints = [[0 for y in range(2)] for x in range(0)]
		
		# H = 0, S = 1, V = 2
		self.targetType = -1
		self.center = [0, 0]
		self.width = 0
		self.height = 0
		
		for point in approx:
			self.center[0] += point[0][0]
			self.center[1] += point[0][1]
		
			if point[0][0] > rightPoints[0][0]:
				rightPoints[1][0] = rightPoints[0][0]
				rightPoints[1][1] = rightPoints[0][1]
			
				rightPoints[0][0] = point[0][0]
				rightPoints[0][1] = point[0][1]
				
			elif point[0][0] > rightPoints[1][0]:
				rightPoints[1][0] = point[0][0]
				rightPoints[1][1] = point[0][1]
				
			elif point[0][1] > upperPoints[0][1]:
				upperPoints[1][0] = upperPoints[0][0]
				upperPoints[1][1] = upperPoints[0][1]

				upperPoints[0][0] = point[0][0]
				upperPoints[0][1] = point[0][1]
			
			elif point[0][1] > upperPoints[1][1]:
				upperPoints[1][0] = point[0][0]
				upperPoints[1][1] = point[0][1]

		self.center[0] /= 4
		self.center[1] /= 4
		
		
		self.width = int(math.sqrt(((upperPoints[0][0] - upperPoints[1][0])**2) + ((upperPoints[0][1] - upperPoints[1][1])**2)))
		self.height = int(math.sqrt(((rightPoints[0][0] - rightPoints[1][0])**2) + ((rightPoints[0][1] - rightPoints[1][1])**2)))

		if width > height and abs(upperPoints[0][1] - upperPoints[1][1]) < self.width * 0.1:
			self.targetType = 0
		if height > width and abs(rightPoints[0][0] - rightPoints[1][0]) < self.height * 0.1:
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
		
