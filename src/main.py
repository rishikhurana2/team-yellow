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
processor = TargetProcessor()
camera = VideoDevice()
cmdinp = ["main.py", "-d", "0", "--no-networking", "--isDebug"]

interface = CmdLineInterface(cmdinp)
config = interface.getConfig()
gui = GUIManager()

camera.startCapture(config.getDeviceID())


if(config.getIsDebug()):
    print("Camera is ready\n")
    #gui.threshWindow()

loop = 1

while(cv2.waitKey(30) != 27):
		
    print ("While Loop %s \n") % loop

    image = camera.getImage()
		
    if(config.getIsDebug()):
        print("Image Read\n")

    detected = detector.TargetDetect(image)
    
    if(config.getIsDebug()):
        print("Image Analyzed\n")
        
    
    if (detector.getFound() == True):
        
        print detected
        
        target = Target(detected)
    	
        if(config.getIsDebug()):
            print("Image Processed by Target Detector\n")
    
        if(config.getIsDebug()):
            print ("Image Being Processed by Target Processor\n")
    
        processor.loadTarget(target)
        
        if(config.getIsDebug()):
            print("Target Loaded\n")
    
        distance = processor.findDistance()
    
        if(config.getIsDebug()):
            print("Distance Calculated\n")
    
        azimuth = processor.findAzimuth()
    
        if(config.getIsDebug()):
            print("Azimuth Calculated\n")
    
        altitude = processor.findAltitude()
    
        if(config.getIsDebug()):
            print("Altitude Calculated\n")
    
        if(config.getIsDebug()):
            print("Image Processed by TargetProcessor\n")
    
        dis = "distance: %s" % distance
        azi = "azimuth: %s" % azimuth
        alt = "altitude: %s" % altitude
        
    else:
        dis = "Not Found"
        azi = "Not Found"
        alt = "Not Found"
    
    gui.setImage(image)
    gui.setText(dis, 1)
    gui.setText(azi, 2)
    gui.setText(alt, 3)
    cv2.imshow("Targeting", gui.getImage())
    loop += 1

cv2.destroyAllWindows()
