import numpy as np
import math

from Target import Target

class TargetProcessor:

	def __init__(self):
		self.rectHeight = 0.02
		self.rectWidth = 0.05
		self.focalLen = 480
		self.horizCent = 240
		self.vertiCent = 320
		
	def loadTarget(self, approx):
		self.dist = 0
		self.azimuth = 0
		self.altitude = 0
		self.targetType = -1

		self.target = Target(approx)
	
		imgWidth = self.target.getWidth()
		imgHeight = self.target.getHeight()
		imgCenter = self.target.getCenter()
		rectCentX = imgCenter[0]
		rectCentY = imgCenter[1]
		offsetX = float(rectCentX - self.horizCent)
		offsetY = float(rectCentY - self.vertiCent)
		self.targetType = self.target.getType()

		self.dist = self.rectWidth * self.focalLen / imgWidth
		self.azimuth = np.arctan(offsetX / self.focalLen) * 180 / math.pi
		self.altitude = np.arctan(offsetY / self.focalLen) * 180 / math.pi

	def getType(self):
		return self.targetType

	def getDistance(self):
		return self.dist

	def getAzimuth(self):
		return self.azimuth

	def getAltitude(self):
		return self.altitude
