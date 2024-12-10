import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']


def plot_scatter_from_csv(csv_file):

    df = pd.read_csv(csv_file)

    x = df.iloc[:, 1]
    y = df.iloc[:, 2]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0, 1])
    plt.xlim([0, 1])
    plt.grid(False)
    plt.show()


csv_file_A = 'D:\\AIM-LAB\\bcc_examples.csv'

# plot_scatter_from_csv(csv_file_A)


def write_image_names_to_csv(folder_path, csv_file_path):
    image_names = [file for file in os.listdir(folder_path) if file.endswith('.jpg') or file.endswith('.png')]

    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for image_name in image_names:
            writer.writerow([image_name])


folder_path_A = 'D:\\AIM-LAB\\BCC\\HuiHuTest2\\other'

csv_file_path_B = 'D:\\AIM-LAB\\bcc_name.csv'

write_image_names_to_csv(folder_path_A, csv_file_path_B)
