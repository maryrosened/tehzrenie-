# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:45:15 2020

@author: нкт
"""

#библиотека opencv
import cv2 
#библиотека массивов 
import numpy as np

def nothing(x):
    pass
  
#включаем камеру  
cam = cv2.VideoCapture(0) 

cv2.namedWindow("Trackbars")

############################# red ###############################
cv2.createTrackbar("Low - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Low - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Low - V", "Trackbars", 0, 255, nothing)

cv2.createTrackbar("High - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("High - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("High - V", "Trackbars", 255, 255, nothing)

   
#ставим разрешение 
frame_width = int(cam.get(3)) 
frame_height = int(cam.get(4))   
size = (frame_width, frame_height) 
   
#записываем эксперимент в файлы '.avi'. 
result = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size) 
result2 = cv2.VideoWriter('outr.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
    
while(True): 
    _, frame = cam.read()
    
    #используем HSV. тон, насыщенность, яркость.
    #H=0-180, S=0-255, V=0-255
    HSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos("Low - H", "Trackbars")
    l_s=cv2.getTrackbarPos("Low - S", "Trackbars")
    l_v=cv2.getTrackbarPos("Low - V", "Trackbars") 
    
    h_h=cv2.getTrackbarPos("High - H", "Trackbars")
    h_s=cv2.getTrackbarPos("High - S", "Trackbars")
    h_v=cv2.getTrackbarPos("High - V", "Trackbars") 
    
    
    #universalcolor
    low=np.array([l_h,l_s,l_v], np.uint8)
    high=np.array([h_h,h_s,h_v], np.uint8)
    uni=cv2.inRange(HSV, low, high)
    unicolor=cv2.bitwise_and(frame, frame, mask=uni)
   
    
    if _ == True:  
  
        #запись на '.avi' 
        result.write(frame) 
        result2.write(unicolor) 
       
        
        #вывод на окно
        cv2.imshow('display', frame)
        cv2.imshow('mask!', unicolor) 
     
  
        #закрываем все через ESC
        ch=cv2.waitKey(5)
        if ch == 27:
            break
  
    #выходим из цикла
    else: 
        break
    
#закрываем окошки  
cam.release() 
result.release()   
cv2.destroyAllWindows() 
   