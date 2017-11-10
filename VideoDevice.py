import cv2
import numpy as np
import math

class VideoDevice:
	def captureDeclare(self):
		global capture
		capture = cv2.VideoCapture(1)
	def feed(self):
		global capture
		cv2.namedWindow("Camera Feed", cv2.WINDOW_AUTOSIZE)
		ret,frame = capture.read()
		cv2.imshow("Camera Feed", frame)
		key = cv2.waitKey(10)
		if key == 27:
			cv2.destroyWindow("Camera Feed")
			break
