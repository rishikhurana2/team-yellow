from CmdLineInterface import CmdLineInterface
from Target import Target
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor
from VideoDevice import VideoDevice
from GUIManager import GUIManager
from AppConfig import AppConfig

import cv2
import sys

detector = TargetDetector()
#processor = TargetProcessor()
camera = VideoDevice()
interface = CmdLineInterface(sys.argv)
config = interface.getConfig()
gui = GUIManager()
processor = TargetProcessor()

camera.captureDeclare(config.getDeviceID())

if(config.getIsDebug()):
	print("Camera is ready\n")
#gui.threshWindow()

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
		processor.loadTarget(detected)

		if config.getIsDebug():
			print ("Image Processed by Target Processor\n")

		targetType = processor.getType()
    
		if config.getIsDebug():
			print("Target Type Calculated\n")

		distance = processor.getDistance()
    
		if config.getIsDebug():
			print("Distance Calculated\n")
    
		azimuth = processor.getAzimuth()
    
		if config.getIsDebug():
			print("Azimuth Calculated\n")
    
		altitude = processor.getAltitude()
    
		if config.getIsDebug():
			print("Altitude Calculated\n")
    
		if config.getIsDebug():
			print("Finished\n")

		typ = "type: %s" % targetType
		dis = "distance: %s" % distance
		azi = "azimuth: %s" % azimuth
		alt = "altitude: %s" % altitude
        
	else:
		typ = "Not Found"
		dis = "N/A"
		azi = "N/A"
		alt = "N/A"
    
	gui.setImage(image)
	gui.setText(typ, 1)
	gui.setText(dis, 2)
	gui.setText(azi, 3)
	gui.setText(alt, 4)
	cv2.imshow("Targeting", gui.getImage())
	loop += 1

cv2.destroyAllWindows()
