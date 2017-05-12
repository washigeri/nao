import numpy as np
import cv2
import cv2.cv as cv


def find_ball(img = None, display = False):
    if img is None:
        img = cv2.imread("camImage.png")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    dim = img.shape
    height = float(dim[1])
    width = float(dim[0])
    scale_ratio = (height / width)
    new_width = 500
    new_height = new_width / scale_ratio
    resized_img = cv2.resize(img, (int(new_width), int(new_height)))
    edges = cv2.Canny(resized_img, 150, 200)
    smooth = cv2.GaussianBlur(edges, (3, 3), 0)
    circles = cv2.HoughCircles(smooth, cv.CV_HOUGH_GRADIENT, 2, 10,  200, 1, minRadius = 5, maxRadius = 50)
    cimg = cv2.cvtColor(smooth, cv2.COLOR_GRAY2BGR)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2], (255, 0, 0), 2)
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    if(display):

        cv2.imshow('test', cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imwrite("result.jpg", cimg)


if __name__ == "__main__":
    find_ball(display=True)
