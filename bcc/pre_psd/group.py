import os
from collections import defaultdict


def contains_keyword_in_name(file_name, keyword):
    return keyword.lower() in file_name.lower()


def count_keyword_combinations(folder_path, keywords_mapping):
    keyword_combinations_count = defaultdict(int)

    for root, dirs, files in os.walk(folder_path):
        keyword_combination = set()
        for file in files:
            file_path = os.path.join(root, file)
            for keyword, destination_subfolder in keywords_mapping.items():
                if contains_keyword_in_name(file, keyword):
                    keyword_combination.add(keyword)

        # 将关键字组合为字符串，用于计数
        keyword_combination_str = '_'.join(sorted(keyword_combination))
        keyword_combinations_count[keyword_combination_str] += 1

    return keyword_combinations_count


parent_folder_path = 'D:/AIM-LAB/BCC/after_mark/name'
keywords_mapping = {
    'leaf-like structures': 'leaf-like structures',
    'blue-grey ovoid nests': 'blue-grey ovoid nests',
    'shiny white structures': 'shiny white structures',
    'ulceration': 'ulceration',
    'spoke wheel structures': 'spoke wheel structures',
    'blue-grey globules': 'blue-grey globules',
    'arborizing vessels': 'arborizing vessels',
}

# 统计每个子文件夹中的图片关键字组合的数量
result = count_keyword_combinations(parent_folder_path, keywords_mapping)

for keyword_combination, count in result.items():
    print(f"关键字组合 '{keyword_combination}': {count} 个")