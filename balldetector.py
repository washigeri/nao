# coding: UTF-8
import cv2
import cv2.cv as cv
import numpy as np
import math

# degrees
NAO_VERTICAL_RADIUS = 47.64
NAO_HORIZONTAL_RADIUS = 60.97
# mm
BALL_RADIUS = 40 / 2
NAO_HEIGHT = 574
NAO_FRONTCAM_HEIGHT = 529
NAO_BOTCAM_HEIGHT = 483


class BallDetector:
    def __init__(self):
        pass

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
                # print math.degrees(vertical_angle), math.degrees(horizontal_angle)
                theta = math.pi - (math.radians(headPitch) + math.pi / 2) - vertical_angle - math.radians(1.2)
                if camera == "bot":
                    theta -= math.radians(39.7)
                # print math.degrees(theta), "°"
                distanceyball = math.tan(theta) * NAO_FRONTCAM_HEIGHT
                distancexball = math.tan(horizontal_angle) * distanceyball
                # print (distancexball, distanceyball), "mm"
                res.append((distancexball, distanceyball))
        return res

    @staticmethod
    def findBalls(img, headpitch_deg):
        red_img = BallDetector.redfilter(img)
        circles = BallDetector.detectCircles(red_img)
        dist_list = BallDetector.computeDistances(circles, red_img.shape, headpitch_deg)
        return dist_list

def main():
    img = cv2.imread("camImage.png")
    bd = BallDetector()
    BallDetector.findBalls(img, 0)

if __name__ == "__main__":
    main()
