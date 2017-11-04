import cv2
import numpy as np
import math
class TargetDetector:
    def TargetDetect(self, img):
        def angle(p1, p2, p0):
            dx1 = p1[0][0]-p0[0][0]
            dy1 = p1[0][1]-p0[0][1]
            dx2 = p2[0][0]-p0[0][0]
            dy2 = p2[0][1]-p0[0][1]
            return math.atan(dy1/dx1)-math.atan(dy2/dx2)

        def right(app, x):
            maxCosine = 0
            for k in range(2, x+1):
                pt1 = app[k%4]
                pt2 = app[k-2]
                pt0 = app[k-1]
                cos = (angle(pt1, pt2, pt0))
                cosine = math.fabs(math.cos(cos))
                maxCosine = max(maxCosine, cosine)
                if(maxCosine<.2):
                    return True
                else:
                    return False
        self.found = False
        count = -1
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        THRESHOLD_MIN = np.array([40, 0, 200],np.uint8)
        THRESHOLD_MAX = np.array([80, 255,255],np.uint8)

        frame = cv2.inRange(img_hsv, THRESHOLD_MIN,THRESHOLD_MAX)
        cv2.imshow("the", frame)
        contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, -1, (255,255,0), 10)
        
        area = 1
        longl = 1
        for cont in contours:
            count = count +1
            epsilon = 0.02*cv2.arcLength(cont,True)
            approx = cv2.approxPolyDP(cont, epsilon, True)
            if cv2.contourArea(approx) > area:
                area = cv2.contourArea(approx)
                longl = len(approx)
            if len(approx) > 3:
            #if right(approx,34):
                print("hiya")
                self.found = True
                return approx
                
                
        print(area)
        print(longl)
    def getFound(self):
        return self.found