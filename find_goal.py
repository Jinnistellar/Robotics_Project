import sys
import cv2

import numpy as np
import math


def findgoal():
	img = cv2.imread("camImage.png",1)
	
	
	print "Width of the image :" + str(img.shape[1]) #width
	print "Height of the image :" + str(img.shape[0]) #height
	 
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	cv2.imshow("HSV Image", hsv)

	lower_yellow=np.array((0,100,80),np.uint8)
	higher_yellow=np.array((180,255,255),np.uint8)
	yellow = cv2.inRange(hsv,lower_yellow, higher_yellow)
	cv2.imshow("Binary Image", yellow)
	
	erode = cv2.erode(yellow,None,iterations = 2)
	cv2.imshow("erode Image", erode)
	
	dilate = cv2.dilate(erode,None,iterations = 3)
	cv2.imshow("dilate Image", dilate)
	
	
#	contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	_,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
	print "Y-axis : Top to bottom"
	print "X-axis : Left to right"
	
	Cx,Cy,W,H,X,Y=0,0,0,0,0,0
	
	maxdiag=0
	
	for cnt in contours:
	    x,y,w,h = cv2.boundingRect(cnt)
	    cx,cy = x+w/2, y+h/2
	    print "Center : ("+ str(cx)+","+str(cy)+") , Width :"+str(w)+", Height :"+str(h)+", Diameter = (Width+Height)/2 : "+str((w+h)/2)
	    cv2.rectangle(img,(x,y),(x+w,y+h),[0,255,255],2)
	
	    if (math.sqrt(w*w+h*h)>maxdiag) :
	     maxdiag=math.sqrt(w*w+h*h)
	     Cx,Cy,W,H,X,Y=cx,cy,w,h,x,y
		
	
	    
	cv2.rectangle(img,(X,Y),(X+W,Y+H),[0,23,255],2)
	print "CENTER : ("+ str(Cx)+","+str(Cy)+") , WIDTH :"+str(W)+", HEIGHT :"+str(H)
	
	y=120 ### Set the value of y over here
	
	Distance= ((y*0.5773)/160)*(160-Cx)
	
	print "Estimated real distance 'x' from the line y to the center of the goal is = "+str(Distance)
	cv2.imshow('goal detected Image',img)
	cv2.waitKey()
	return Distance
