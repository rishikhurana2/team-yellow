import cv2

class GUIManager:
    
    def __init__(self):
        cv2.namedWindow("Targeting", cv2.WINDOW_AUTOSIZE)
    
    def threshWindow(self):
        cv2.namedWindow("Thresh", cv2.WINDOW_AUTOSIZE)

    def setImage(self, inputImage):
        self.image = inputImage
        
    def setText(self, imageText, row):
        cv2.putText(self.image, imageText, (10, 400 + (row*20)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)
    
    def getImage(self):
        return self.image
