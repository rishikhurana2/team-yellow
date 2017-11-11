import cv2

class VideoDevice:
	camera = None
	def captureDeclare(self, camID):
		self.camera = cv2.VideoCapture(camID)
	
	def getFrame(self):
		ret,frame = self.camera.read()
		return frame
