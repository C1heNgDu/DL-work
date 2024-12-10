import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Function to be called whenever the trackbar is moved
def update_threshold(threshold_value):
    _, thresholded = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow('Thresholded Image', thresholded)

image = cv2.imread("D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\arborizing vessels orin train test\\Huanshuitang_meijering_black_sigma_[1, 2, 3, 4].png")
# image = cv2.imread("D:/test.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

test = np.uint8(gray_image)
clahe = cv2.createCLAHE(clipLimit=4, tileGridSize=(3,3))
test_clahe = clahe.apply(test)
cv2.imwrite('D:/test.png',gray_image)


cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)

cv2.imshow('Original Image', test_clahe)

cv2.namedWindow('Thresholded Image', cv2.WINDOW_NORMAL)

initial_threshold = 128

cv2.createTrackbar('Threshold', 'Thresholded Image', initial_threshold, 255, update_threshold)
update_threshold(initial_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
