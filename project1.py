import cv2 
import numpy as np
import time

cap = cv2.VideoCapture(0)

img = cv2.imread("download.jpg")

while True: 
    ret, frame = cap.read()
    if not ret:
        break 
    frame = cv2.resize(frame,(640,480))
    img = cv2.resize(img,(640,480))

    lower_black = np.array([200,200,200])
    upper_black = np.array([255,255,255])
    mask_1 = cv2.inRange(frame,lower_black,upper_black)

    res_2 = cv2.bitwise_and(frame,frame,mask=mask_1)

    f = frame - res_2
    f = np.where(f ==0, img , f)

    cv2.imshow("magic", frame)
    cv2.imshow("mask", f)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()


   
