import cv2
import numpy as np
cv2.NamedWindow("Camera Feed", cv2.CV_WINDOW_AUTOSIZE)
capture = cv2.CaptureFromCAM(0)
while True:
    frame = cv2.QueryFrame(capture)
    cv2.ShowImage("Camera Feed", frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyWindow("preview")

