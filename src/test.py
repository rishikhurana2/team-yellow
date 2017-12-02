from TargetProcessor import TargetProcessor

import cv2
import sys

arr = [[[1, 0]], [[0, 2]], [[4, 4]], [[5, 2]]]

processor = TargetProcessor()
processor.loadTarget(arr)

print(str(processor.getAltitude()))
