import os
import time

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

from mask_rcnn import MASK_RCNN


if __name__ == "__main__":
    mask_rcnn = MASK_RCNN()
    mode = "dir_predict"
    video_path = 0
    video_save_path = ""
    video_fps = 25.0
    test_interval = 100
    fps_image_path = "img/3927754171_9011487133_b.jpg"
    # dir_origin_path = "datasets/dataset_hh/JPEGImages"
    dir_origin_path = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\test\\screening"
    dir_save_path = "img1_0315-1/"

    if mode == "predict":

        while True:
            img = input('Input image filename:')
            try:
                image = Image.open(img)
            except:
                print('Open Error! Try again!')
                continue
            else:
                r_image = mask_rcnn.detect_image(image)
                r_image.show()

    elif mode == "dir_predict":
        import os
        from tqdm import tqdm

        img_names = os.listdir(dir_origin_path)
        for img_name in tqdm(img_names):
            if img_name.lower().endswith(
                    ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                image_path = os.path.join(dir_origin_path, img_name)
                image = Image.open(image_path)
                r_image = mask_rcnn.detect_image(image)
                if not os.path.exists(dir_save_path):
                    os.makedirs(dir_save_path)
                r_image.save(os.path.join(dir_save_path, img_name.replace(".jpg", ".png")), quality=95, subsampling=0)

    else:
        raise AssertionError("Please specify the correct mode: 'predict', 'video', 'fps' or 'dir_predict'.")
