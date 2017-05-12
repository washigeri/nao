import numpy as np
import cv2
import cv2.cv as cv
import imutils


def main():
    img = cv2.imread("camImage.png")
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.medianBlur(gray, 5)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3.5)
    kernel = np.ones((2.6, 2.7), np.uint8)
    gray = cv2.erode(gray, kernel, iterations=1)
    gray = cv2.dilate(gray, kernel, iterations=1)
    circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1.2, 260, param1=30, param2=65, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.round(circles[0, :].astype("int"))
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
