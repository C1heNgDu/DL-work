import cv2
import os

# 定义文件夹路径
folder_path = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\arborizing vessels\\arborizing vessels val orin"

# 定义输出文件夹路径
output_folder = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\arborizing vessels\\11"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 设置CLAHE参数
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 遍历文件夹中的所有图像文件
for filename in os.listdir(folder_path):
    # 检查文件扩展名是否为图像格式
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # 图像文件路径
        image_path = os.path.join(folder_path, filename)

        # 读取图像
        image = cv2.imread(image_path)

        # 转换图像为HSV颜色空间
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 提取S通道
        s_channel = hsv_image[:, :, 1]

        # 对S通道应用CLAHE增强
        enhanced_s_channel = clahe.apply(s_channel)

        # 更新HSV图像的S通道
        hsv_image[:, :, 1] = enhanced_s_channel

        # 将图像转换回RGB颜色空间
        enhanced_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

        # 保存增强后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, enhanced_image)
        print(f"Enhanced image saved: {output_path}")
