from algorithm.object_detector import YOLOv7
from utils.detections import draw
import json
import cv2

yolov7 = YOLOv7()
yolov7.load('pre2.pt', classes='coco.yaml', device='gpu') # use 'gpu' for CUDA GPU inference

webcam = cv2.VideoCapture("test.mp4")

if webcam.isOpened() == False:
	print('[!] error opening the webcam')

try:
    while webcam.isOpened():
        ret, frame = webcam.read()
        if ret == True:
            detections = yolov7.detect(frame)
            for detection in detections:
             print("Class:", detection['class'])
             print("Confidence:", detection['confidence'])
             print("x:", detection['x'])
             print("y:", detection['y']) 
             if detection["confidence"] > 0.7:
              detected_frame = draw(frame, detections)
              cv2.imshow('webcam', detected_frame)
             else:
               cv2.imshow('webcam', frame)
            cv2.waitKey(1)
        else:
            break
except KeyboardInterrupt:
    pass

webcam.release()
print('[+] webcam closed') 
yolov7.unload()
