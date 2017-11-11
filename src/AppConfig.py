class AppConfig:
	def __init__(self):
		self.deviceID = 0
		self.isFile = 0
		self.isDevice = 0
		self.isHeadless = 0
		self.isNetworking = 1
		self.isDebug = 0

	def getDeviceID(self):
		return self.deviceID
	
	def getIsFile(self):
		return self.isFile

	def getIsDevice(self):
		return self.isDevice

	def getIsHeadless(self):
		return self.isHeadless

	def getIsNetworking(self):
		return self.isNetworking

	def getIsDebug(self):
		return self.isDebug

	def setDeviceID(self, num):
		self.deviceID = num

	def setIsFile(self, num):
		self.isFile = num

	def setIsDevice(self, num):
		self.isDevice = num

	def setIsHeadless(self, num):
		self.isHeadless = num

	def setIsNetworking(self, num):
		self.isNetworking = num

	def setIsDebug(self, num):
		self.isDebug = num
