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

	def setDeviceID(self, inp1):
		self.deviceID = inp1
	def setIsFile(self, inp2):
		self.isFile = inp2
	def setIsDevice(self, inp3):
		self.isDevice = inp3
	def setIsHeadless(self, inp4):
		self.isHeadless = inp4
	def setIsNetworking(self, inp5):
		self.isNetworking = inp5
	def setIsDebug(self, inp6):
		self.isDebug = inp6

