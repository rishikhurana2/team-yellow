import numpy as np
import math

from Target import Target

class TargetProcessor:

	def __init__(self, approx):
		imgWidth = 0
		imgHeight = 0
		dist = 0
		azimuth = 0
		altitude = 0
		targetType = -1

		rectHeight = 0.02
		rectWidth = 0.05
		focalLen = 480
		horizCent = 240
		vertiCent = 320
    
		self.target = Target(approx)

	def loadTarget(self):
		imgWidth = self.target.getWidth()
		imgHeight = self.target.getHeight()
		imgCenter = self.target.getCenter()
		rectCentX = imgCenter[0]
		rectCentY = imgCenter[1]
		offsetX = float(rectCentX - horizCent)
		offsetY = float(-1 * (rectCentY - vertiCent))
		targetType = self.target.getType()

		dist = self.rectWidth * self.focalLen / imgWidth
		azimuth = np.arctan(offsetX / self.focalLen) * 180 / math.pi
		altitude = np.arctan(offsetY / self.focalLen) * 180 / math.pi

	def getType(self):
		return self.targetType

	def getDistance(self):
		return self.dist

	def getAzimuth(self):
		return self.azimuth

	def getAltitude(self):
		return self.altitude
