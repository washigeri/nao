# coding: UTF-8
import cv2
import cv2.cv as cv
import numpy as np
import math
import os.path

# degrees
NAO_VERTICAL_RADIUS = 47.64
NAO_HORIZONTAL_RADIUS = 60.97
# mm
BALL_RADIUS = 40 / 2
NAO_HEIGHT = 574
NAO_FRONTCAM_HEIGHT = 529
NAO_BOTCAM_HEIGHT = 483


#used for computing the focal length
DISTANCE_FROM_CAMERA = 1120
BALL_DIAMETER = 40
FOCAL_LENGTH = 0


class BallDetector:
    def __init__(self):
        pass

    @staticmethod
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
        focalLength = (2 * r * DISTANCE_FROM_CAMERA) / BALL_DIAMETER
        return focalLength

    @staticmethod
    def getFocalLength():
        filename = "../img/calibrate/fl.txt"
        if os.path.isfile(filename):
            file = open(filename, 'r')
            focalLength = int(file.read())
            file.close()
        else:
            file = open(filename, 'w')
            focalLength = BallDetector.computeFocalLength()
            file.write(str(focalLength))
            file.close()
        return focalLength

    @staticmethod
    def setFocalLength():
        global FOCAL_LENGTH
        FOCAL_LENGTH = BallDetector.getFocalLength()


    @staticmethod
    def distance_to_camera(knownWidth, focalLength, perceivedWidth):
        return (knownWidth * focalLength) / perceivedWidth


    @staticmethod
    def redfilter(img):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 65, 50])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
        mask = mask0 + mask1
        output_img = img.copy()
        output_img[np.where(mask == 0)] = 0
        return output_img

    @staticmethod
    def detectCircles(img):
        # output = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((7, 7), np.uint8)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        circles = cv2.HoughCircles(image=gray, method=cv.CV_HOUGH_GRADIENT, dp=1, minDist=100, param1=100, param2=1,
                                   minRadius=10, maxRadius=50)
        if circles is not None:
            # print "ok"
            circles = np.round(circles[0, :].astype("int"))
            # for (x, y, r) in circles:
            #    cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            #    cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        return circles

    # @staticmethod
    # def computeDistances(circles, img_shape, headPitch, camera=""):
    #     res = None
    #     if circles is not None and img_shape is not None:
    #         res = []
    #         x_mid = img_shape[1] / 2
    #         y_mid = img_shape[0] / 2
    #         vertical_angle_rad = math.radians(NAO_VERTICAL_RADIUS)
    #         horizontal_angle_rad = math.radians(NAO_HORIZONTAL_RADIUS)
    #         for (x, y, r) in circles:
    #             distcenterx = float(x - x_mid)
    #             distcentery = float(y - y_mid)
    #             vertical_angle = (distcentery / img_shape[1]) * vertical_angle_rad
    #             horizontal_angle = (distcenterx / img_shape[0]) * horizontal_angle_rad
    #             # print math.degrees(vertical_angle), math.degrees(horizontal_angle)
    #             theta = math.pi - (math.radians(headPitch) + math.pi / 2) - vertical_angle - math.radians(1.2)
    #             if camera == "bot":
    #                 theta -= math.radians(39.7)
    #             # print math.degrees(theta), "°"
    #             distanceyball = math.tan(theta) * NAO_FRONTCAM_HEIGHT
    #             distancexball = math.tan(horizontal_angle) * distanceyball
    #             # print (distancexball, distanceyball), "mm"
    #             res.append((distancexball, distanceyball))
    #     return res

    @staticmethod
    def computeDistances(circles, img_shape, headPitch, camera=""):
        res = None
        if circles is not None and img_shape is not None:
            res = []
            x_mid = img_shape[1] / 2
            y_mid = img_shape[0] / 2
            vertical_angle_rad = math.radians(NAO_VERTICAL_RADIUS)
            horizontal_angle_rad = math.radians(NAO_HORIZONTAL_RADIUS)
            for (x, y, r) in circles:
                distcenterx = float(x - x_mid)
                distcentery = float(y - y_mid)
                vertical_angle = (distcentery / img_shape[1]) * vertical_angle_rad
                horizontal_angle = (distcenterx / img_shape[0]) * horizontal_angle_rad
                distance = BallDetector.distance_to_camera(BALL_DIAMETER, FOCAL_LENGTH, r*2)
                theta = math.pi - (math.radians(headPitch) + math.pi / 2) - vertical_angle - math.radians(1.2)
                if camera == "bot":
                    theta -= math.radians(39.7)
                distance_floor = distance * math.sin(theta)
                distancex = distance_floor * math.cos(math.pi / 2 - horizontal_angle)
                distancey = math.sqrt(distance_floor ** 2 - distancex ** 2)
                print(distancex, distancey)
                res.append((distancex, distancey))
        return  res

    @staticmethod
    def computeAngles_bot(circles, img_shape):
        res = None
        if circles is not None and img_shape is not None:
            res =[]
            x_mid = img_shape[1] / 2
            y_mid = img_shape[0] / 2
            vertical_angle_rad = math.radians(NAO_VERTICAL_RADIUS)
            horizontal_angle_rad = math.radians(NAO_HORIZONTAL_RADIUS)
            for (x,y,r) in circles:
                distcenterx = float(x - x_mid)
                distcentery = float(y - y_mid)
                vertical_angle = (distcentery / img_shape[1]) * vertical_angle_rad
                horizontal_angle = (distcenterx / img_shape[0]) * horizontal_angle_rad
                # print math.degrees(vertical_angle), math.degrees(horizontal_angle)
                res.append((vertical_angle, horizontal_angle))
        return  res

    @staticmethod
    def findBalls(img, headpitch_deg):
        BallDetector.setFocalLength()
        red_img = BallDetector.redfilter(img)
        circles = BallDetector.detectCircles(red_img)
        dist_list = BallDetector.computeDistances(circles, red_img.shape, headpitch_deg)
        return dist_list

    @staticmethod
    def finBalls_bot(img):
        red_img = BallDetector.redfilter(img)
        circles = BallDetector.detectCircles(red_img)
        angles_list = BallDetector.computeAngles_bot(circles, red_img.shape)
        return angles_list

def main():
    BallDetector.setFocalLength()
    img = cv2.imread('../img/test/balle_rouge_lumiere.png')
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    red = BallDetector.redfilter(img)
    circles = BallDetector.detectCircles(red)
    #BallDetector.computeDistances(circles, img.shape, 0, camera="")
    BallDetector.computeAngles_bot(circles, img.shape)


if __name__ == "__main__":
    main()