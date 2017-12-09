'''Target Attributes

Calculates width, height, and the coordinates for the center of the target.
'''

import cv2
import math

class Target:
	def __init__(self, approx):
		'''Calculates all attributes
		
		First find the two points at the top of the target and the right of the target.
		Then use Pythagorean Theorem to calculate width and height. We use Pythagorean Theorem to calculate
		distance between two points in case the rectangle is slanted.
		To find the center coordinate we just take the average of all of the X and Y coordinates.
		'''
	
		upperPoints = [[0 for y in range(2)] for x in range(2)]
		rightPoints = [[0 for y in range(2)] for x in range(2)]
		
		self.targetType = -1 # Horizontal = 0, Spinning = 1, Vertical = 2
		
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
				
			if point[0][1] > upperPoints[0][1]:
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

		if self.width > self.height and abs(upperPoints[0][1] - upperPoints[1][1]) < self.width * 0.1:
			self.targetType = 0
		elif self.height > self.width and abs(rightPoints[0][0] - rightPoints[1][0]) < self.height * 0.1:
			self.targetType = 2
		else:
			self.targetType = 1


	def getType(self):
		'''Returns target type'''
	
		return self.targetType


	def getWidth(self):
		'''Returns width of target'''
	
		return self.width


	def getHeight(self):
		'''Returns height of target'''
	
		return self.height


	def getCenter(self):
		'''Returns center coordinate of target'''
	
		return self.center
		
