
import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)


    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    x     = 0.6
    y     = 0.2
    theta = 0.0

    # This example show customization for the both foot
    # with all the possible gait parameters
    try:
        motionProxy.moveTo(x, y, theta,
            [ ["MaxStepX", 0.03],         # step of x cm infront
              ["MaxStepY", 0.16],         #
              ["MaxStepTheta", 0.4],      #
              ["MaxStepFrequency", 0.0],  # low frequency
              ["StepHeight", 0.01],       # step height of x cm
              ["TorsoWx", 0.0],           # 
              ["TorsoWy", 0.0] ])         # torso bend x rad in front
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.2.112",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
