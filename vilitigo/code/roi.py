import os
import cv2
import numpy as np


def process_image(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([11, 55, 46])
    upper_yellow = np.array([25, 255, 255])
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    image[yellow_mask > 0] = [0, 0, 0]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 150])
    upper_white = np.array([180, 90, 255])  # 80 , 100
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #white_mask

    mask = np.zeros(gray.shape, dtype=np.uint8)

    cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)
    result = cv2.bitwise_and(image, image, mask=mask)

    output_path = os.path.splitext(image_path)[0] + '_ori.png'
    cv2.imwrite(output_path, result)


def process_image_extract(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([11, 55, 46])
    upper_yellow = np.array([25, 255, 255])
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    image[yellow_mask > 0] = [0, 0, 0]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 255)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros(gray.shape, dtype=np.uint8)

    cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)

    result = cv2.bitwise_and(image, image, mask=mask)

    kernel = np.ones((3, 3), np.uint8)
    eroded_image = cv2.erode(result, kernel, iterations=-1)
    mask = np.all(eroded_image == [255, 255, 255], axis=-1)

    eroded_image[mask] = [0, 0, 0]

    output_path = os.path.splitext(image_path)[0] + '_org.png'
    cv2.imwrite(output_path, eroded_image)


def find_and_replace_contours(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 150])
    upper_white = np.array([180, 90, 255])  # 80 , 100

    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    contours, _ = cv2.findContours(white_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros_like(gray_image)

    cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)

    image_with_contours = image.copy()
    image_with_contours[mask == 255] = (0, 0, 0)

    cv2.drawContours(image, contours, -1, (0, 0, 255), 2)

    output_path = os.path.splitext(image_path)[0] + '_ert.png'
    cv2.imwrite(output_path, image_with_contours)


folder_path = r'D:\\after_mark1\\wangye'
subfolders = os.listdir(folder_path)

for subfolder in subfolders:
    subfolder_path = os.path.join(folder_path, subfolder)
    image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith('contour.png')]
    for image_file in image_files:
        image_path = os.path.join(subfolder_path, image_file)
        process_image(image_path)

for subfolder in subfolders:
    subfolder_path = os.path.join(folder_path, subfolder)
    image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith('_ori.png')]
    for image_file in image_files:
        image_path = os.path.join(subfolder_path, image_file)
        process_image_extract(image_path)

for subfolder in subfolders:
    subfolder_path = os.path.join(folder_path, subfolder)
    image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith('_org.png')]
    for image_file in image_files:
        image_path = os.path.join(subfolder_path, image_file)
        find_and_replace_contours(image_path)

