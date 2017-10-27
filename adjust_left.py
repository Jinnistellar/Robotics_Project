#-*- coding: iso-8859-15 -*-
import argparse
import sys
import math
import almath as m
from naoqi import ALProxy
import find_goal
import find_ball

'''Walk To: Small example to make Nao Walk To an Objective '''
'''         With customization '''

    
def StiffnessOn(proxy):
    pNames="Body"
    pStiffnessLists=1.0
    pTimeLists=1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
    
    
def main(robotIP,PORT=9559):
    try:
        motionProxy = ALProxy("ALMotion",robotIP, PORT)
        postureProxy=ALProxy("ALRobotPosture",robotIP, PORT)

    except Exception, e:
        print "couldnt connect proxy to ALMotion"
        print "Error was: ",e

    # Set NAO in stiffness On
    
    
    D=find_goal.findgoal()
    
    theta =math.atan(D/120)
    x     = 0.3*(1-math.cos(theta))
    y     = -0.3*(math.sin(theta))

    if D>30 or D<-(30):
        theta=math.atan(D/120)
        

   # parameters are set to the default value
    motionProxy.walkTo(x, y, theta) # step height of 4 cm
    StiffnessOn(motionProxy)

if __name__ == "__main__":
    robotIP="192.168.2.109"
    PORT=9559
    if len(sys.argv) <= 1:
        print "Usage python motion_moveTo.py robotIP"
    else:
        robotIp = sys.argv[1]
    main(robotIP)
    
    
