import cv2

class Target:
	def putDistance(self,distance):
		global dist
		dist = distance
	def putAzimuth(self,azimuth):
		global az
		az = azimuth
	def putAltitude(self,altitude):
		global alt
		alt = altitude
	def getDistance(self):
		global dist
		return dist
	def getAzimuth(self):
		global az
		return azimuth
	def getAltitude(self):
		global alt
		return alt
