from AppConfig import AppConfig

class CmdLineInterface:
    def printUsage(self):
        print( "Usage: program (-d <device_num>) [--no-networking] [--headless] [--debug]")

    def __init__(self, inargs):
        self.config = AppConfig()
        self.cmdnum = 3
        if (inargs[1] == "-d"):
            self.config.setIsDevice(1)
            idnum = (int)(inargs[2])
            self.config.setDeviceID(idnum)
        else:
            self.printUsage()

        if (len(inargs) > 3):
            count = 0
            for darg in inargs:
                if (darg == "--no-networking"):
                    self.config.setIsNetworking(0)

                elif (darg == "--headless"):
                    self.config.setIsHeadless(1)

                elif (darg == "--isDebug"):
                    self.config.setIsDebug(1)
                    
                else:
                    if (count > 2):
                        print("noonon")
                        self.printUsage()
                        break

        else:
            self.printUsage()
			
    def getConfig(self):
        return self.config
	