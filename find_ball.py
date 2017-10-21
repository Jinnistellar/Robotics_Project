import sys
import cv2
import numpy as np
import math


# function for detecting the ball of yellow
def findball() :
        img = cv2.imread("camImage1.png",1)
        
        #cv2.namedWindow("HSV Image",cv2.CV_WINDOW_AUTOSIZE)
        #cv2.namedWindow("Binary Image",cv2.CV_WINDOW_AUTOSIZE)
        
        #cv2.namedWindow("dilate Image",cv2.CV_WINDOW_AUTOSIZE)
        #cv2.namedWindow("goal detected Image",cv2.CV_WINDOW_AUTOSIZE)
        
        print "Width of the image :" + str(img.shape[1]) #width
        print "Height of the image  :" + str(img.shape[0]) #height
         
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV Image", hsv)
        
        blue = cv2.inRange(hsv,np.array([100,100,100],np.uint8),np.array([130,255,255],np.uint8))
        cv2.imshow("Binary Image", blue)
        
        erode = cv2.erode(blue,None,iterations = 1)
        cv2.imshow("erode Image", erode)
        
        dilate = cv2.dilate(erode,None,iterations = 5)
        cv2.imshow("dilate Image", dilate)
        cv2.waitKey()
        
        #######################################
        smoothing=cv2.blur(blue,(10,10))
        dilate = cv2.dilate(smoothing,None,iterations = 3)
        #storage=cv2.CreateMemStorage(0)
        #dilate=camImage.fromarray(dilate)
       # circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,2.5,200,100,25,0)
        circles = cv2.HoughCircles(np.asarray(dilate), cv2.HOUGH_GRADIENT, 100, 300, 100, 50)
        ##########################################
        
        _,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        print "Y-axis : Top to bottom"
        print "X-axis : Left to right"
        
        Cx,Cy,W,H,X,Y=0,0,0,0,0,0
        maxdiag=0

        
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            cx,cy = x+w/2, y+h/2
            print "Center : ("+ str(cx)+","+str(cy)+") , Width :"+str(w)+", Height :"+str(h)+", Radius = (Width+Height)/2 : "+str((w+h)/2)
            if 20 < hsv.item(cy,cx,0) < 30:
                    cv2.rectangle(img,(x,y),(x+w,y+h),[0,255,255],2)
            if (math.sqrt(w*w+h*h)>maxdiag) :
                        maxdiag=math.sqrt(w*w+h*h)
                        Cx,Cy,W,H,X,Y=cx,cy,w,h,x,y
        
            
        
        
        cv2.rectangle(img,(X,Y),(X+W,Y+H),[0,23,255],2)
        print "CENTER : ("+ str(Cx)+","+str(Cy)+") , WIDTH :"+str(W)+", HEIGHT :"+str(H)
        cv2.imshow('Ball detected Image',img)
        cv2.waitKey()
        
        front =0
        if (Cy<130):
                print "move one step in front"
                front =1

        if (Cx>135 and Cx<160): 
            print "Move right to adjust"
            return [0,front]
        elif Cx > 225:
            return [5,front]
        elif (Cx>160 and Cx<185): 
            print "Move left to adjust"
            return [1,front]
        elif Cx < 95 :
            return [4,front]
        elif Cx<160:
         #   print "\nKick using LEFT Foot"
            return [2,front]
        elif Cx>160:
    #    print "\nKick using RIGHT Foot"
            return [3,front]

if __name__ == '__main__':
  
  IP = "192.168.2.112"              # IP add
  PORT = 9559

  # Read IP address from first argument if any.
  if len(sys.argv) > 1:
    IP = sys.argv[1]

  ball = findball()

