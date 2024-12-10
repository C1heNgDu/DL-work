from PIL import Image
import os

# 输入文件夹路径
input_folder = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\need'
# 输出文件夹路径
output_folder = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\need1'

# 遍历输入文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # 添加需要处理的图片格式
        # 构建输入图片的完整路径
        input_path = os.path.join(input_folder, filename)

        # 打开图片
        img = Image.open(input_path)

        # 创建一个相同尺寸的纯黑图片
        black_img = Image.new('RGB', img.size, (0, 0, 0))

        # 构建输出图片的完整路径
        output_path = os.path.join(output_folder, filename)

        # 保存纯黑图片
        black_img.save(output_path)

        # 关闭输入图片
        img.close()

print("生成纯黑图片完成。")

for filename in os.listdir(output_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # 添加需要处理的图片格式
        # 构建输入图片的完整路径
        input_path = os.path.join(output_folder, filename)

        # 获取文件名（不包含后缀）
        file_name, file_extension = os.path.splitext(filename)

        # 构建输出图片的完整路径，将后缀改为png
        output_path = os.path.join(output_folder, file_name + '.png')

        # 重命名文件
        os.rename(input_path, output_path)

print("图片后缀修改完成。")