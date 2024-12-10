import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import data
from skimage.filters import threshold_multiotsu

def clahe_image(image_path, output_image):
    img = cv2.imread(image_path, 0)
    clahe = cv2.createCLAHE(clipLimit=2.0)
    gray_image_clahe = clahe.apply(img)
    clahe.setClipLimit(2.0)
    img = clahe.apply(img)

    cv2.imwrite(output_image, img)

def multi_Otsu(image_path, output_path):
    image = cv2.imread(image_path, 0)
    thresholds = threshold_multiotsu(image)
    regions = np.digitize(image, bins=thresholds)
    plt.figure()
    plt.imshow(regions, cmap='jet')
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight')

    plt.show()

def resized_image(image_path, output_path):
    img = cv2.imread(image_path)

    width = 4608
    height = 3456
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    cv2.imwrite(output_path, resized_img)



if __name__ == "__main__":
    folder_path = r'D:\1\4\1'
    subfolders = os.listdir(folder_path)
    
    # clahe
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith('.png')]
        for image_file in image_files:
            try:
                image_path = os.path.join(subfolder_path, image_file)
                output_path = os.path.splitext(image_path)[0] + '_clahe2.0.png'
                clahe_image(image_path, output_path)

            except Exception as e:
                print(f"处理子文件夹 {subfolder} 时出错: {str(e)}")
    
    # multi_otsu
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith('clahe2.0.png')]
        for image_file in image_files:
            try:
                image_path = os.path.join(subfolder_path, image_file)
                output_path = os.path.splitext(image_path)[0] + '_size.png'
                multi_Otsu(image_path, output_path)

            except Exception as e:
                print(f"处理子文件夹 {subfolder} 时出错: {str(e)}")
    
    # resize images
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith('size.png')]
        for image_file in image_files:
            try:
                image_path = os.path.join(subfolder_path, image_file)
                output_path = os.path.splitext(image_path)[0] + '_otsu.png'
                resized_image(image_path, output_path)

            except Exception as e:
                print(f"处理子文件夹 {subfolder} 时出错: {str(e)}")
