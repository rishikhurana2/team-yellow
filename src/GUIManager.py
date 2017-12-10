'''GUI Manager

Manages all graphical outputs.
'''


import cv2


class GUIManager:
    def __init__(self):
        '''Initializes the default window'''
    
        cv2.namedWindow("Targeting", cv2.WINDOW_AUTOSIZE)

    
    def threshWindow(self):
        '''Initializes thresholded image window for debug mode'''
    
        cv2.namedWindow("Thresh", cv2.WINDOW_AUTOSIZE)


    def setImage(self, inputImage):
        '''Sets the image for the default window'''
    
        self.image = inputImage

        
    def setText(self, imageText, row):
        '''Places text onto the image on the bottom right
        
        Row range from 1-4
        '''
    
        cv2.putText(self.image, imageText, (10, 390 + (row * 20)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)

    
    def getImage(self):
        '''Returns the formatted image'''
    
        return self.image
