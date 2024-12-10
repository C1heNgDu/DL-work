import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def draw_contours_and_save(image_path, output_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=cv2.FILLED)
    cv2.imwrite(output_path, img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img_rgb)
    # plt.title('Contours')
    # plt.show()


def process_images_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            draw_contours_and_save(input_path, output_path)


input_folder = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\shiny white structures  mask train-1"
output_folder = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\shiny white structures mask train-2"
process_images_in_folder(input_folder, output_folder)



