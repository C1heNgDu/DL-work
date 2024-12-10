import os
import random
import shutil


def copy_matching_images(source_folder, matching_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_name, source_file_extension = os.path.splitext(file)
            source_file_path = os.path.join(root, file)
            matching_file_path = os.path.join(matching_folder, source_file_name + ".*")
            destination_file_path = os.path.join(destination_folder, file)

            # 在 D:/B 中查找匹配的文件
            matching_files = [f for f in os.listdir(matching_folder) if f.startswith(source_file_name)]

            if matching_files:
                # 选择匹配文件中的第一个文件进行复制
                matching_file_name = matching_files[0]
                matching_file_path = os.path.join(matching_folder, matching_file_name)
                shutil.copy2(matching_file_path, destination_file_path)
                print(f"已复制：{matching_file_path} 到 {destination_file_path}")


# 随机抽取10%的图片
def copy_random_images(source_folder, destination_folder_B, destination_folder_C, percentage=10):
    all_files = os.listdir(source_folder)
    num_files_to_copy_B = int(len(all_files) * (percentage / 100.0))
    files_to_copy_B = random.sample(all_files, num_files_to_copy_B)
    if not os.path.exists(destination_folder_B):
        os.makedirs(destination_folder_B)

    if not os.path.exists(destination_folder_C):
        os.makedirs(destination_folder_C)
    for file_name in files_to_copy_B:
        source_path = os.path.join(source_folder, file_name)
        destination_path_B = os.path.join(destination_folder_B, file_name)
        shutil.copy2(source_path, destination_path_B)
    for file_name in all_files:
        if file_name not in files_to_copy_B:
            source_path = os.path.join(source_folder, file_name)
            destination_path_C = os.path.join(destination_folder_C, file_name)
            shutil.copy2(source_path, destination_path_C)


# 修改图片名，只留下名字
def rename_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = '_'.join(file.split('_')[:2]) + '.png'

            new_file_path = os.path.join(root, new_file_name)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"已重命名：{old_file_path} 到 {new_file_path}")


def rename_images_in_subfolders(parent_folder):
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            file_path = os.path.join(root, file)
            folder_name = os.path.basename(root)
            new_file_name = f"{folder_name}_{file}"
            new_file_path = os.path.join(root, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"已重命名：{file_path} 到 {new_file_path}")

if __name__ == '__main__':
    # parent_folder_path = 'D:\\AIM-LAB\\BCC\\after_mark\\5'
    # rename_images_in_subfolders(parent_folder_path)

    # source_folder_path = 'D:/AIM-LAB/BCC/after_mark/2/ulceration mask'
    matching_folder_path = 'D:/AIM-LAB/BCC/basal cell carcinoma'

    source_folder_path = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\ulceration orin\\new'
    # matching_folder_path = 'D:\\paycharm-work\\tf_2\\mask-rcnn-tf2-master\\datasets\\dataset_hh\\JPEGImages'
    # matching_folder_path = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\blue-grey ovoid nests\\blue-grey ovoid nests mask'
    destination_folder_path = 'D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\ulceration orin\\new orin'
    copy_matching_images(source_folder_path, matching_folder_path, destination_folder_path)
    #
    # source_folder = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\shiny white structures"
    # destination_folder_B = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\shiny white structures mask val"
    # destination_folder_C = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\shiny white structures mask train"
    #
    # copy_random_images(source_folder, destination_folder_B, destination_folder_C, percentage=10)

