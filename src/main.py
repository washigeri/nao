# from naoqi import ALProxy
# import sys
# import time
# import Image_perso
# import vision_definitions
# import cv2
# import numpy
# import Image
# import balldetector
#
# NAO_IP = "localhost"
# NAO_PORT = 9559
#
#
#
# def showNaoImage(IP, PORT):
#   """
#   First get an image from Nao, then show it on the screen with PIL.
#   """
#
#   camProxy = ALProxy("ALVideoDevice", IP, PORT)
#   resolution = 2    # VGA
#   colorSpace = 11   # RGB
#
#   videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
#
#   t0 = time.time()
#
#   # Get a camera image.
#   # image[6] contains the image data passed as an array of ASCII chars.
#   naoImage = camProxy.getImageRemote(videoClient)
#
#   t1 = time.time()
#
#   # Time the image transfer.
#   print "acquisition delay ", t1 - t0
#
#   camProxy.unsubscribe(videoClient)
#
#
#   # Now we work with the image returned and save it as a PNG  using ImageDraw
#   # package.
#
#   # Get the image size and pixel array.
#   imageWidth = naoImage[0]
#   imageHeight = naoImage[1]
#   array = naoImage[6]
#
#   # Create a PIL Image from our pixel array.
#   im = Image.fromstring("RGB", (imageWidth, imageHeight), array)
#
#   # Save the image.
#   im.save("camImage.png", "PNG")
#
#   Image_perso.find_ball(numpy.array(im))
#
#
#
# def main():
#     print "Creating ALVideoDevice proxy to :", NAO_IP
#
#     resolution = vision_definitions.k4VGA
#     colorSpace = vision_definitions.kBGRColorSpace
#     fps = 10
#
#     nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
#     print nameId
#     print  "getting images in local"
#
#
# if __name__ == "__main__":
#     showNaoImage(NAO_IP, NAO_PORT)
import cv2

import balldetector

img = cv2.imread("camImage.png")
balldetector.BallDetector.findBalls(img, 0)