from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(600, 450)):
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有图片文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 打开图像文件
            with Image.open(input_path) as img:
                # 将图像resize到目标尺寸
                resized_img = img.resize(target_size, Image.ANTIALIAS)

                # 保存resize后的图像
                resized_img.save(output_path)

if __name__ == "__main__":
    # 设置输入和输出文件夹路径
    input_folder = "D:/AIM-LAB/BCC/after_mark/seven/mask/arborizing vessels orin"
    output_folder = "D:/AIM-LAB/BCC/after_mark/seven/mask/arborizing vessels orin_resized"

    # 设置目标尺寸
    target_size = (600, 450)

    # 执行resize操作
    resize_images(input_folder, output_folder, target_size)
