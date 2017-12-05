'''Application Configuration

Stores the settings for the program
'''

class AppConfig:
	def __init__(self):
		self.deviceID = 0
		self.isFile = 0
		self.isDevice = 0
		self.isHeadless = 0
		self.isNetworking = 1
		self.isDebug = 0


	def getDeviceID(self):
	'''Returns the camera ID'''
	
		return self.deviceID
	
	
	def getIsFile(self):
	'''Returns the image name'''
	
		return self.isFile


	def getIsDevice(self):
    '''Returns if there is a camera'''
    
		return self.isDevice


	def getIsHeadless(self):
	'''Returns if running as headless'''
	
		return self.isHeadless


	def getIsNetworking(self):
	'''Returns if running with networking'''
	
		return self.isNetworking


	def getIsDebug(self):
	'''Returns if running debug mode'''
	
		return self.isDebug


	def setDeviceID(self, num):
	'''Changes the camera ID'''
	
		self.deviceID = num


	def setIsFile(self, num):
	'''Changes the image name'''
	
		self.isFile = num


	def setIsDevice(self, num):
	'''Changes if there is a camera or not'''
	
		self.isDevice = num


	def setIsHeadless(self, num):
	'''Changes if running as headless or not'''
	
		self.isHeadless = num


	def setIsNetworking(self, num):
	'''Changes if running with networking or not'''
	
		self.isNetworking = num


	def setIsDebug(self, num):
	'''Changes if running on debug mode or not'''
	
		self.isDebug = num
