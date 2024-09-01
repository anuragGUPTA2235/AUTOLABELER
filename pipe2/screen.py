import os
from algorithm.object_detector import YOLOv7
import rospy
from std_msgs.msg import Float32MultiArray, String
from utils.detections import draw
import json
import cv2
from cv_bridge import CvBridge
import imutils
import numpy as np
from mss import mss
from PIL import Image



sct = mss()
image = None
store = None
frame_counter = 0
image_folder = "images"





yolov7 = YOLOv7()
yolov7.load('pre2.pt', classes='coco.yaml', device='gpu') # use 'gpu' for CUDA GPU inference




try:
    while True:
        w, h = 640, 480
        monitor = {'top': 185, 'left': 675, 'width': w, 'height': h}
        img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
        img_np = np.array(img)
        frame = img_np
        frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)    
        detections = yolov7.detect(frame)
        detected_frame = draw(frame, detections)
     

        frame_filename = os.path.join(image_folder, f"frame_{frame_counter}.jpg")
        if store is not None:
            print(store)
            cv2.imwrite(frame_filename, detected_frame)
            frame_counter += 1
            store = None
        
        cv2.imshow('webcam', detected_frame)
        cv2.waitKey(1)
        
except KeyboardInterrupt:
    pass
webcam.release()
print('[+] webcam closed')
yolov7.unload()
