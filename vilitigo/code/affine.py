import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import glob


def extract_green_features(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([50, 43, 50])
    upper_green = np.array([99, 255, 250]) # 180 250
    # lower_white = np.array([0, 0, 221])
    # upper_white = np.array([180, 30, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    return green_mask


def find_target_contour(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    target_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            target_contour = contour

    return target_contour


def affine_image_registration(image1_path, image2_path, output_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    green_features1 = extract_green_features(image1)
    green_features2 = extract_green_features(image2)

    kernel = np.ones((3, 3), np.uint8)

    green_features1 = cv2.dilate(green_features1, kernel, iterations=1)
    green_features2 = cv2.dilate(green_features2, kernel, iterations=1)

    target_contour1 = find_target_contour(green_features1)
    target_contour2 = find_target_contour(green_features2)

    x1, y1, w1, h1 = cv2.boundingRect(target_contour1)
    x2, y2, w2, h2 = cv2.boundingRect(target_contour2)

    print(w1, h1, w2, h2)

    if w1 > h1 and w2 > h2:
        scale_factor = w1 / w2
    else:
        scale_factor = h1 / h2

    print(scale_factor)

    scaled_image2 = cv2.resize(image2, None, fx=scale_factor, fy=scale_factor)
    scaled_height, scaled_width = scaled_image2.shape[:2]

    height, width = image2.shape[:2]

    height_diff = height - scaled_height
    width_diff = width - scaled_width

    top = height_diff // 2
    bottom = height_diff - top
    left = width_diff // 2
    right = width_diff - left

    if height_diff >= 0 and width_diff >= 0:
        padded_image2 = cv2.copyMakeBorder(scaled_image2, top, bottom, left, right, cv2.BORDER_CONSTANT,
                                           value=[0, 0, 0])
        cropped_image2 = padded_image2[:height, :width]
    elif height_diff < 0 and width_diff < 0:
        cropped_image2 = scaled_image2[abs(top):scaled_height - abs(top), abs(left):scaled_width - abs(left)]
        cv2.imwrite(output_path, cropped_image2)
    else:
        print("尺寸差异方向不一致，无法处理")
        cropped_image2 = None

    if cropped_image2 is not None:
        cv2.imwrite(output_path, cropped_image2)
    else:
        print("无法生成配准后的图像")

    green_features3 = extract_green_features(cropped_image2)
    target_contour3 = find_target_contour(green_features3)
    x3, y3, w3, h3 = cv2.boundingRect(target_contour3)


affine_image_registration('D:\\A.png', 'D:\\B.png','D:\\B_affine.png')


