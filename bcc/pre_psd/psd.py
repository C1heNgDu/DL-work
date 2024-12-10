import os
from psd_tools import PSDImage
from glob import glob
from PIL import Image

'''psd_name=glob("D:/AIM-LAB/BCC/after_mark/1-9/ISIC_0011403.psd") # 对应的保存文件的路径

for i in range(len(psd_name)):
    psd = PSDImage.open(psd_name[i])
    psd[0].visible=False
    psd.compose(True).save("D:/AIM-LAB/BCC/after_mark/1-9/"+psd_name[i].split("/")[-1].split(".")[0]+".png")  #True这个参数一定要有，上边的隐藏语句才有效，不然还是合并了全部图层可见。

psd = PSDImage.open('D:/AIM-LAB/BCC/after_mark/1-9/ISIC_0011141.psd')
def extractLayerImge(layer):
    layer_image = layer.composite()

    layer_image.save('D:/AIM-LAB/BCC/after_mark/1-9/%s.png' % layer.name)

for layer in psd.descendants():
    print('descendants ', layer)

    extractLayerImge(layer)'''


def extract_layers(input_psd_path, output_folder):

    psd = PSDImage.open(input_psd_path)
    os.makedirs(output_folder, exist_ok=True)

    for i, layer in enumerate(psd):

        width, height = psd.width, psd.height
        new_image = Image.new("RGB", (width, height), (255, 255, 255))
        new_image.paste(layer.compose())
        output_path = os.path.join(output_folder, f"layer_{i + 1}.png")
        new_image.save(output_path)

def merge_and_save_layers(input_psd_path, output_folder):
    psd = PSDImage.open(input_psd_path)
    os.makedirs(output_folder, exist_ok=True)
    psd[0].visible = False
    for i, layer in enumerate(psd):
        for l in psd:
            l.visible = False
        layer.visible = True
        composed_image = psd.compose(True)
        save_path = os.path.join(output_folder, f"layer_{i}.png")
        composed_image.save(save_path)

if __name__ == "__main__":
    '''input_psd_path = 'D:/AIM-LAB/BCC/after_mark/1-9/ISIC_0011642.psd'
    output_folder = 'D:/AIM-LAB/BCC/after_mark/1-9/ISIC_0011642_output'
    merge_and_save_layers(input_psd_path, output_folder)'''

    input_folder = 'D:/AIM-LAB/BCC/after_mark/1'
    output_parent_folder = 'D:/AIM-LAB/BCC/after_mark/5'
    for psd_file in os.listdir(input_folder):
        if psd_file.endswith(".psd"):
            input_psd_path = os.path.join(input_folder, psd_file)
            output_folder = os.path.join(output_parent_folder, psd_file.split('.')[0])
            merge_and_save_layers(input_psd_path, output_folder)