import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def hsv_extract(image_path, output_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 43, 46]) 
    upper_blue = np.array([124, 255, 255]) 
    lower_cyan = np.array([78, 43, 46]) 
    upper_cyan = np.array([99, 255, 255])
    lower_white = np.array([0, 0, 210]) 
    upper_white = np.array([180, 30, 255]) 

    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    white_pixel_count_blue = cv2.countNonZero(mask_blue)
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)
    white_pixel_count_white = cv2.countNonZero(mask_white)

    if white_pixel_count_blue < white_pixel_count_white:
        # Set mask_blue to black
        image[mask_blue == 255] = 0
        mask_blue[:] = 0

    mask_cyan = cv2.inRange(hsv_image, lower_cyan, upper_cyan)
    white_pixel_count_cyan = cv2.countNonZero(mask_cyan)

    if abs(white_pixel_count_cyan - white_pixel_count_white) < 1000:
        image[mask_cyan == 255] = 0
        mask_cyan[:] = 0
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

    has_black_white_blue_cyan = (np.any(mask_cyan) and np.any(mask_blue))
    has_black_white_cyan = (np.all(mask_blue == 0))
    has_black_white_blue = (np.all(mask_cyan == 0))
    #print(has_black_white_blue_cyan, has_black_white_cyan, has_black_white_blue)
    if has_black_white_blue_cyan:
        image[mask_blue == 255] = 0
        image[mask_cyan == 255] = 255
    elif has_black_white_cyan:
        image[mask_cyan == 255] = 255
        image[mask_blue == 255] = 0
    elif has_black_white_blue:
        image[mask_blue == 255] = 255
        image[mask_cyan == 255] = 0

    cv2.imwrite(output_path, image)

def replace(image_path, output_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image[gray != 0] = 255
    cv2.imwrite(output_path, image)

def threshold(image_path, output_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    red_image = cv2.bitwise_and(image, image, mask=mask)
    gray = cv2.cvtColor(red_image, cv2.COLOR_BGR2GRAY)
    red_image[gray != 0] = 255
    gray_image = cv2.cvtColor(red_image, cv2.COLOR_BGR2GRAY)  # convert the image to grayscale

    cv2.imwrite(output_path, gray_image)

hsv_extract('D:/170116 (4)_affine_ori_org_ert_binary.png', 'D:/170116 (4)_affine_ori_org_ert_binary_2.png')
