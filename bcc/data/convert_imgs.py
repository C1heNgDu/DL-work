from PIL import Image
import os

# 定义文件夹路径
folder_a = 'D:\\paycharm-work\\tf_2\\mask-rcnn-tf2-master\\0315\\5'
# folder_b = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\test\\screening-test'
folder_b = 'D:\\paycharm-work\\tf_2\\mask-rcnn-tf2-master\\0315\\2'

image_files_a = os.listdir(folder_a)

for image_file_a in image_files_a:
    image_a = Image.open(os.path.join(folder_a, image_file_a))
    pixels_a = image_a.load()

    image_b = Image.open(os.path.join(folder_b, image_file_a))
    pixels_b = image_b.load()

    width_a, height_a = image_a.size

    for y in range(height_a):
        for x in range(width_a):
            r, g, b = pixels_a[x, y]
            # 5[240,150,133] 4[246,201,87] 3[220,233,244] 2[171,208,241] 1[158,196,190]
            # 5ulceration[0,103,166] 1arborizing vessels[0,171,216] 2blue-grey globules[0,137,114] 4shiny white structures
            # [245,197,100] 3blue-grey ovoid nests[242,87,45]
            if (r, g, b) == (0,103,166):
                # 在B图片上覆盖目标颜色
                pixels_b[x, y] = (r, g, b)

    image_b.save(os.path.join(folder_b, image_file_a))

