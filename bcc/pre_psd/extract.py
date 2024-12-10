from PIL import Image
import os
import re
import cv2


def process_images(parent_folder):
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if file.lower().endswith(".jpg") and file.lower() != "layer_0.png":
                image_path = os.path.join(root, file)
                '''if file.lower().startswith("layer"):
                    parent_folder_name = os.path.basename(root)
                    print(parent_folder_name)'''
                # process_image(image_path)
                # update_name(image_path, os.path.basename(root) + "_" + file)
                # update_name3(image_path)
                # black_red(image_path)
                # convert_image(image_path,file)
                new_image_path = change_image_extension(image_path, ".png")
                # change_extension_to_jpg(image_path)


# 一次性去掉_layer_1
def update_name(image_path, new_filename):
    directory, filename = os.path.split(image_path)
    new_filename = re.sub(r'_arborizing vessels_layer_+\d', '', filename)
    new_path = os.path.join(directory, new_filename)
    os.rename(image_path, new_path)


# 修改文件名去掉layer, ISIC_000001_layer_1.png-->ISIC_000001_1.png
def update_name1(image_path, new_filename):
    directory = os.path.dirname(image_path)
    new_filename = new_filename.replace("layer_", "")
    new_path = os.path.join(directory, new_filename)
    os.rename(image_path, new_path)


# 去掉最后两个字符_1
def update_name3(image_path):
    directory, filename = os.path.split(image_path)
    base_filename, file_extension = os.path.splitext(filename)
    new_base_filename = base_filename[:-2]
    new_filename = new_base_filename + file_extension
    new_path = os.path.join(directory, new_filename)
    os.rename(image_path, new_path)

# 修改文件名，按照颜色对应特征
def process_image(image_path):
    image = Image.open(image_path).convert("RGBA")

    has_transparent_pixels = any(pixel[3] == 0 for pixel in image.getdata())
    name_updated = False
    if has_transparent_pixels:
        for pixel in image.getdata():
            if pixel[3] != 0:
                if not name_updated:
                    if pixel[:3] == (161, 138, 98):
                        update_image_name(image_path, "leaf-like structures")
                    elif pixel[:3] == (64, 62, 98):
                        update_image_name(image_path, "blue-grey ovoid nests")
                    elif pixel[:3] == (238, 135, 162):
                        update_image_name(image_path, "shiny white structures")
                    elif pixel[:3] == (250, 241, 243):
                        update_image_name(image_path, "ulceration")
                    elif pixel[:3] == (9, 238, 90):
                        update_image_name(image_path, "spoke wheel structures")

                name_updated = True


def change_extension_to_jpg(image_path):
    directory, filename = os.path.split(image_path)
    new_filename, _ = os.path.splitext(filename)
    new_filename += ".jpg"
    new_path = os.path.join(directory, new_filename)
    os.rename(image_path, new_path)


def update_image_name(image_path, new_name):
    directory, filename = os.path.split(image_path)

    new_filename = new_name + "_" + filename

    old_path = image_path
    new_path = os.path.join(directory, new_filename)

    try:
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        else:
            print(f"File not found: {old_path}")
    except Exception as e:
        print(f"Error renaming file: {e}")


# 修改文件名，按照颜色对应特征
def black_red(image_path):
    image = Image.open(image_path)
    filename = os.path.basename(image_path)
    if filename.lower().startswith("layer"):
        print(filename)
        hsv_image = image.convert("HSV")
        red_range_lower = (156, 43, 46)
        red_range_upper = (180, 255, 255)
        black_range_lower = (0, 0, 0)
        black_range_upper = (180, 255, 46)

        has_red = any(
            any(red_range_lower[j] <= pixel[j] <= red_range_upper[j] for j in range(3))
            for pixel in hsv_image.getdata()
        )
        print(has_red)
        has_black = any(
            any(black_range_lower[j] <= pixel[j] <= black_range_upper[j] for j in range(3))
            for pixel in hsv_image.getdata()
        )
        print(has_black)
        if has_red:
            update_image_name(image_path, "arborizing vessels")
        if has_black:
            update_image_name(image_path, "blue-grey globules")


# 将非0像素点替换为白色
def convert_image(image_path, output_path):
    img = cv2.imread(image_path)
    _, img_binary = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    # img_binary[img_binary != 0] = 255
    cv2.imwrite(output_path, img_binary)


def change_image_extension(image_path, new_extension):
    img = cv2.imread(image_path)
    file_name, file_extension = os.path.splitext(image_path)
    new_image_path = file_name + ".png"
    cv2.imwrite(new_image_path, img)

    return new_image_path


if __name__ == "__main__":
    parent_folder = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\test\\screening-test"
    process_images(parent_folder)
