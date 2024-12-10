import cv2
import numpy as np
from PIL import Image, ImageOps

def find_first_green_pixel(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        cnt = max(contours, key=cv2.contourArea)
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return cx, cy
    return None

#Calculate the rotation angle
def calculate_rotation_angle(img_a, img_b):
    green_pixel_a = find_first_green_pixel(img_a)
    green_pixel_b = find_first_green_pixel(img_b)

    if green_pixel_a is None or green_pixel_b is None:
        return None

    angle = np.arctan2(green_pixel_a[1] - green_pixel_b[1], green_pixel_a[0] - green_pixel_b[0]) * 180 / np.pi
    return angle

#rotate the follow up image
def rotate_and_crop(image_path, angle_degrees):
    original_image = Image.open(image_path)
    angle_radians = np.radians(angle_degrees)

    new_width = int(np.ceil(np.abs(original_image.width * np.cos(angle_radians)) + np.abs(original_image.height * np.sin(angle_radians))))
    new_height = int(np.ceil(np.abs(original_image.width * np.sin(angle_radians)) + np.abs(original_image.height * np.cos(angle_radians))))

    rotated_image = original_image.rotate(angle_degrees, resample=Image.BICUBIC, expand=False)

    left = (new_width - original_image.width) // 2
    top = (new_height - original_image.height) // 2
    right = left + original_image.width
    bottom = top + original_image.height

    cropped_image = rotated_image.crop((left, top, right, bottom))

    return cropped_image

if __name__ == "__main__":

    A_path = "First.png"
    B_path = "FollowUp.png"
    img_a = cv2.imread(A_path)
    img_b = cv2.imread(B_path)

    rotation_angle = calculate_rotation_angle(img_a, img_b)
    output_image_path = "b_rotate.png"

    resize_and_crop(B_path, output_image_path, rotation_angle)

