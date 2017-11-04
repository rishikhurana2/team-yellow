import cv2

class VideoDevice:
    camera = None
    def startCapture(self, id):
        self.camera = cv2.VideoCapture(id)

    def getImage(self):
        ret, image = self.camera.read()
        return image


	

