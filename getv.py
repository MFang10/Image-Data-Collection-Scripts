import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1) # video capture source camera (Here external usb webcam. default laptop camera: 0) 
cap.set(3, 1920); # Frame height resolution
cap.set(4, 1080); # Frame width resolution

counter = 0
capture_duration = 180 # video duration in seconds
start_time = time.time()

while(int(time.time() - start_time) < capture_duration ):
    ret,frame = cap.read() 
    frame_name = "c" + str(counter) + ".png"
    cv2.imwrite(frame_name,frame) # written to script directory
    
    cv2.imshow('img1',frame)
    cv2.waitKey(30) # frame interval = 30ms
    counter += 1

cv2.destroyAllWindows()
cap.release()
