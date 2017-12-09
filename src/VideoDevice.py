'''Video Device Manager

Manages all things pertaining to the camera.
'''

import cv2

class VideoDevice:
	camera = None
	
	def cameraDeclare(self, camID):
		'''Creates a camera using inputted ID'''
	
		self.camera = cv2.VideoCapture(camID)
	
	
	def getFrame(self):
		'''Grabs image from camera'''
	
		ret,frame = self.camera.read()
		return frame
