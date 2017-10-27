# Choregraphe bezier export in Python.
#import config
import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

  names = list()
  times = list()
  keys = list()
  
  names.append("LHipYawPitch")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ -0.00456, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ -0.00456, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("LHipRoll")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ 0.13810, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ 0.13810, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("LHipPitch")
  times.append([ 2.60000, 5.00000, 5.20000])
  keys.append([ [ -0.28528, [ 3, -0.86667, 0.00000], [ 3, 0.80000, 0.00000]], [ -0.56549, [ 3, -0.80000, 0.11092], [ 3, 0.06667, -0.00924]], [ -0.64577, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("LKneePitch")
  times.append([ 2.60000, 5.00000, 5.20000])
  keys.append([ [ 1.02007, [ 3, -0.86667, 0.00000], [ 3, 0.80000, 0.00000]], [ 1.91812, [ 3, -0.80000, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.02007, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("LAnklePitch")
  times.append([ 2.60000, 5.00000, 5.20000])
  keys.append([ [ -0.69955, [ 3, -0.86667, 0.00000], [ 3, 0.80000, 0.00000]], [ -0.46251, [ 3, -0.80000, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.69955, [ 3, -0.06667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("LAnkleRoll")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ 0.00311, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ 0.00311, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("RHipRoll")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ 0.11202, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ 0.11202, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("RHipPitch")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ -0.20253, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ -0.20253, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("RKneePitch")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ 0.83761, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ 0.83761, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("RAnklePitch")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ -0.45862, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ -0.45862, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

  names.append("RAnkleRoll")
  times.append([ 2.60000, 5.20000])
  keys.append([ [ -0.23466, [ 3, -0.86667, 0.00000], [ 3, 0.86667, 0.00000]], [ -0.23466, [ 3, -0.86667, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  IP="192.168.2.108"
  motion = ALProxy("ALMotion", IP, 9559)
 # motion = config.loadProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.2.104",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
