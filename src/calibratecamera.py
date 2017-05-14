import cv2
import cv2.cv as cv
import numpy as np


# F = (P x D) / W
DISTANCE_FROM_CAMERA = 1120
BALL_DIAMETER = 40
# def redfilter(img):
#     img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower_red = np.array([0, 255, 100])
#     upper_red = np.array([10, 255, 255])
#     mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
#     lower_red = np.array([170, 50, 50])
#     upper_red = np.array([180, 255, 255])
#     mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
#     mask = mask0 + mask1
#     output_img = img.copy()
#     output_img[np.where(mask == 0)] = 0
#     return output_img
#
# def detectCircles(img):
#        output = img.copy()
#        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#        kernel = np.ones((13, 13), np.uint8)
#        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
#        gray = cv2.GaussianBlur(gray, (3, 3), 0)
#        circles = cv2.HoughCircles(image=gray, method=cv.CV_HOUGH_GRADIENT, dp=1, minDist=100, param1=100, param2=1,
#                                   minRadius=10, maxRadius=15)
#        if circles is not None:
#            # print "ok"
#            circles = np.round(circles[0, :].astype("int"))
#            for (x, y, r) in circles:
#              cv2.circle(output, (x, y), r, (0, 255, 0), 4)
#              cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#        return (output, circles[0][2])
#
#
#
# IMAGE_PATHS = ["../img/calibrate/5.jpg", "../img/calibrate/10.jpg", "../img/calibrate/15.jpg",
#                "../img/calibrate/25.jpg"]
#
# image = cv2.imread(IMAGE_PATHS[0])
#
# red = redfilter(image)
#
# #balls = BallDetector.detectCircles(red)
#
# circles, r = detectCircles(red)
#
# focalLength = (2*r * DISTANCE_FROM_CAMERA) / BALL_DIAMETER
# print focalLength, "mm"
#
# cv2.imshow("test", circles)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



def computeFocalLength():
    img = cv2.imread("../img/calibrate/5.jpg")
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 255, 100])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    mask = mask0 + mask1
    output_img = img.copy()
    output_img[np.where(mask == 0)] = 0
    gray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((13, 13), np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    circles = cv2.HoughCircles(image=gray, method=cv.CV_HOUGH_GRADIENT, dp=1, minDist=100, param1=100, param2=1,
                               minRadius=10, maxRadius=15)
    circles = np.round(circles[0, :].astype("int"))
    r = circles[0][2]
    focalLength = (2*r * DISTANCE_FROM_CAMERA) / BALL_DIAMETER
    return focalLength


