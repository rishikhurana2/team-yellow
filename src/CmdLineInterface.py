'''Command Line Input Parsing

Parses apart the command line input and stores the settings into the AppConfig class.
'''

from AppConfig import AppConfig


class CmdLineInterface:
	def printUsage(self):
		'''Prints out the format for the command line input'''

		print( "Usage: program (-d <device_num>) [--no-networking] [--headless] [--debug]")


	def __init__(self, argv):
		'''Parsing the input command line array and inputting it into the AppConfig object'''

		self.config = AppConfig()

		if len(argv) == 1 or len(argv) == 2:
			self.printUsage()			
			return

		if argv[1] == "-d":
			self.config.setIsDevice(1)
			self.config.setDeviceID(int(argv[2]))
		else:
			self.printUsage()
			return

		if len(argv) > 3:
			for x in range(3, len(argv)):
				if argv[x] == "--no-networking" or argv[x] == "-n":
					self.config.setIsNetworking(0)

				elif argv[x] == "--headless" or argv[x] == "-h":
					self.config.setIsHeadless(1)

				elif argv[x] == "--debug" or argv[x] == "-d":
					self.config.setIsDebug(1)

				else:
					print("Invalid argument")
					self.printUsage()
					break


	def getConfig(self):
		'''Returns the configured AppConfig object'''
	
		return self.config
	
