import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import re
import glob


def find_contour_area(image_path, mode):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    edges = cv2.Canny(image, 10, 255)

    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if mode == "external":
        contours = [contour for contour in contours if cv2.isContourConvex(contour)]
    elif mode == "internal":
        contours = [contour for contour in contours if not cv2.isContourConvex(contour)]

    total_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area

    return total_area



def calculate_zhuoselv(image_path1, image_path2):

    img1 = cv2.imread(image_path1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img2 = cv2.imread(image_path2, 0)

    hist1, _ = np.histogram(img1.ravel(), 256, [0, 256])
    hist2, _ = np.histogram(img2.ravel(), 256, [0, 256])

    total_pixels = img1.size

    zero_count1 = hist1[0]

    print(zero_count1)

    white_count2 = hist2[255]
    print(white_count2)

    illness = total_pixels - zero_count1

    zhuoselv =1- (white_count2) / illness

    return zhuoselv

def extract_number_from_filename(filename):

    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

def process_subfolder(subfolder_path):
    image_files = [f for f in os.listdir(subfolder_path) if f.endswith('.png')]
    image_files.sort(key=lambda x: extract_number_from_filename(x))

    results = []
    output_path = os.path.join(subfolder_path, 'results2.txt')
    for i in range(0, len(image_files), 2):
        image1 = image_files[i]
        if i + 1 < len(image_files):
            image2 = image_files[i + 1]
            image_path1 = os.path.join(subfolder_path, image1)
            image_path2 = os.path.join(subfolder_path, image2)
            if "recover" in image1:
                repigmentation_rate = 1.0
            else:
                repigmentation_rate = calculate_zhuoselv(image_path1, image_path2)

            results.append(repigmentation_rate)

            img = cv2.imread(image_path1)

            cv2.putText(img, 'Repigmentation rate: {:.2f}'.format(repigmentation_rate), (200, 3000), cv2.FONT_HERSHEY_SIMPLEX, 4,
                        (255, 255, 255), 2)
            image_name = os.path.splitext(os.path.basename(image_path1))[0]
            output_path_with_text = os.path.join(subfolder_path, image_name + '_with_text.png')
            cv2.imwrite(output_path_with_text, img)
            image_number = extract_number_from_filename(image1)
            with open(output_path, 'a') as file:  # Use 'a' to append to the file
                file.write(f'{image_number}: {repigmentation_rate:.2f}\n')


folder_path = r'D:/after_mark1'
subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

for subfolder in subfolders:
    subfolder_path = os.path.join(folder_path, subfolder)
    process_subfolder(subfolder_path)