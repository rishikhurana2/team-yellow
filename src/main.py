'''Main Program

Structure:
Creates and initializes all classes
Begins infinite loop
	Processes image and returns data if target is located
	Sends data to java client
	Shows output image from GUI Manager
Cleanup
'''

import cv2
import sys

from AppConfig import AppConfig
from CmdLineInterface import CmdLineInterface
from GUIManager import GUIManager
from Network import Network
from Target import Target
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from VideoDevice import VideoDevice


interface = CmdLineInterface(sys.argv)
detector = TargetDetector()
processor = TargetProcessor()
camera = VideoDevice()

config = interface.getConfig()

network = None


if config.getIsNetworking():
	global network
	network = Network()
	network.userServer()

camera.cameraDeclare(config.getDeviceID())

if(not config.getIsHeadless()):
	gui = GUIManager()
	gui.threshWindow()

if(config.getIsDebug()):
	print("Camera is ready\n")


loop = 1

while cv2.waitKey(30) != 27:	
	print ("While Loop: " + str(loop))

	image = camera.getFrame()
	if config.getIsDebug():
		print("Image Read\n")

	detected = detector.contour(detector.threshold(image))
	if config.getIsDebug():
		print("Image Analyzed\n")

	if detector.getFound() == True:
		if config.getIsDebug():
			print ("Target Found\n")
	
		processor.loadTarget(detected)
		if config.getIsDebug():
			print ("Image Processed by Target Processor\n")

		targetType = processor.getType()
		if config.getIsDebug():
			print("Target Type Calculated\n")

		if config.getIsDebug():
			print("Distance Calculated\n")
			
		azimuth = processor.getAzimuth()
		if config.getIsDebug():
			print("Azimuth Calculated\n")

		if config.getIsDebug():
			print("Altitude Calculated\n")

		if config.getIsDebug():
			print("Finished\n")

		typ = "type: %s" % targetType
		azi = "azimuth: %s" % azimuth
		
		if config.getIsNetworking():
			network.setType(str(targetType))
			network.setAzimuth(str(azimuth))
  
	else:
		typ = "Not Found"
		azi = "N/A"

	if(not config.getIsHeadless()):
		gui.setImage(image)
		gui.setText(typ, 2)
		gui.setText(azi, 3)
		cv2.imshow("Targeting", gui.getImage())
	
	loop += 1

cv2.destroyAllWindows()
