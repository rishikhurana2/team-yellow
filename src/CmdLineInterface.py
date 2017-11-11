from AppConfig import AppConfig

class CmdLineInterface:
	def printUsage(self):
		print( "Usage: program (-d <device_num>) [--no-networking] [--headless] [--debug]")

	def __init__(self, argv):
		self.config = AppConfig()

		if len(argv) == 1:
			self.printUsage()			
			return

		if argv[1] == "-d":
			self.config.setIsDevice(1)
			self.config.setDeviceID(int(argv[2]))
		else:
			self.printUsage()
			return

		if len(argv) > 3:
			for arg in range(3, len(argv)):
				if arg == "--no-networking" or arg == "-n":
					self.config.setIsNetworking(0)

				elif arg == "--headless" or arg == "-h":
					self.config.setIsHeadless(1)

				elif arg == "--debug" or arg == "-d":
					self.config.setIsDebug(1)
    
				else:
					print("Invalid argument")
					self.printUsage()
					break

	def getConfig(self):
		return self.config
	
