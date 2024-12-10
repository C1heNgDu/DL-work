import json


def remove_empty_list_section(file_path):
    while True:
        with open(file_path, 'r') as file:
            data = file.read()

        start_index = data.find("[]")

        if start_index != -1:
            start_bracket_index = data.rfind("{", 0, start_index)
            end_bracket_index = data.find("}", start_index)

            if start_bracket_index != -1 and end_bracket_index != -1:
                end_index = data.find(",", end_bracket_index)
                if end_index != -1:
                    new_data = data[:start_bracket_index] + data[end_index + 1:]
                else:
                    new_data = data[:start_bracket_index]

                with open(file_path, 'w') as output_file:
                    output_file.write(new_data)
                    print("已移除一个空列表所在的大括号内的内容及其后的一个逗号")
            else:
                print("未找到符合条件的内容")
        else:
            print("未找到包含 '[]' 的位置")
            break  # 如果找不到了就退出循环


# 请将 'your_file.json' 替换为你实际的 JSON 文件路径
remove_empty_list_section('G:/IT/PYTHON/MASKRCNN/mask-rcnn-tf2-master/datasets/dataset_hh/Jsons/val_annotations.json')
