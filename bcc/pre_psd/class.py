import os
import shutil
from PIL import Image


def contains_keyword_in_name(file_name, keyword):
    return keyword.lower() in file_name.lower()


# 移动到对应文件夹
def process_images(source_folder, destination_folder, keywords_mapping):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            for keyword, destination_subfolder in keywords_mapping.items():
                if contains_keyword_in_name(file, keyword):
                    destination_path = os.path.join(destination_folder, destination_subfolder)
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy(file_path, destination_path)
                    break


source_folder_path = 'D:/AIM-LAB/BCC/after_mark/5'
destination_folder_path = 'D:/AIM-LAB/BCC/after_mark/6'
keywords_mapping = {
    'leaf-like structures': 'leaf-like structures',
    'blue-grey ovoid nests': 'blue-grey ovoid nests',
    'shiny white structures': 'shiny white structures',
    'ulceration': 'ulceration',
    'spoke wheel structures': 'spoke wheel structures',
    'blue-grey globules': 'blue-grey globules',
    'arborizing vessels': 'arborizing vessels',
}

process_images(source_folder_path, destination_folder_path, keywords_mapping)
