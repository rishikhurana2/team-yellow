import numpy as np
import math

from Target import Target
class TargetProcessor:
    RectHeight = 0
    RectWidth = 0
    focalLen = 0
    horizCent = 0
    vertiCent = 0
    imgWidth = 0
    imgHeight = 0
    def __init__(self):
        global RectHeight
        global RectWidth
        global focalLen
        global horizCent
        global vertiCent
        RectHeight = 0.02
        RectWidth = 0.05
        focalLen = 480
        horizCent = 240
        vertiCent = 320
    def loadTarget(self, target):
        global imgWidth
        global imgHeight
        global offsetX
        global offsetY
        imgWidth = target.getWidth()
        imgHeight = target.getHeight()
        imgCenter = target.getCenter()
        RectcentX = imgCenter[0]
        RectcentY = imgCenter[1]
        offsetX = float(RectcentX - horizCent)
        offsetY = float(-1*(RectcentY - vertiCent))
        

    def findDistance(self):
        if imgWidth == 0:
            return (0)
        else:
            dist = RectWidth * focalLen / imgWidth
            return (dist)

    def findAzimuth(self):
        azimuth = np.arctan(offsetX/ focalLen)*180/math.pi
        return (azimuth)

    def findAltitude(self):
        altit = np.arctan(offsetY/ focalLen)*180/math.pi
        return (altit)