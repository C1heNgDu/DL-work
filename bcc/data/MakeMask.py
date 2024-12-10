from PIL import Image
import os
import numpy as np
import cv2


# Change the image extension to '.png'
def change_image_extension(folder_path, new_extension=".jpg"):
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".gif", ".bmp", ".png")):
            original_file_path = os.path.join(folder_path, filename)
            new_filename = os.path.splitext(filename)[0] + new_extension
            new_file_path = os.path.join(folder_path, new_filename)

            os.rename(original_file_path, new_file_path)
            print(f"Renamed: {filename} to {new_filename}")


def generate_mask_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
            img = cv2.imread(input_path)
            height, width = img.shape[:2]
            mask = np.zeros((height, width), dtype=np.uint8)
            cv2.imwrite(output_path, mask)


# change_image_extension(folder_A_path)
input_folder = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\test\\other_no_ul'
output_folder = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\no_ul'
generate_mask_images(input_folder, output_folder)
