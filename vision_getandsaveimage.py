# Get an image from NAO. Display it and save it using PIL.

import sys
import time

# Python Image Library
import Image
import config
import cv
#import vision_definations
from naoqi import ALProxy


def showNaoImage(IP, PORT,camera_id):
  """
  First get an image from Nao, then show it on the screen with PIL.
  """
  # Select the lower camera
  camProxy = config.loadProxy("ALVideoDevice")
  camProxy.kCameraSelectID=18
  print camProxy.getParam(camProxy.kCameraSelectID)
  camProxy.setParam(camProxy.kCameraSelectID,camera_id)
#  print camProxy.getParam(camProxy.kCameraSelectID)

  
  
  resolution =  1   # VGA
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  naoImage = camProxy.getImageRemote(videoClient)

  t1 = time.time()

  # Time the image transfer.
  print "acquisition delay ", t1 - t0

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Create a PIL Image from our pixel array.
  im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Save the image.
  im.save("camImage.png", "PNG")

  im.show()



if __name__ == '__main__':
  IP = "192.168.2.104"  # Replace here with your NaoQi's IP address.
  PORT = 9559

  # Read IP address from first argument if any.
  if len(sys.argv) > 1:
    IP = sys.argv[1]

  showNaoImage(IP, PORT)

