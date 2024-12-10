import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools
import cv2  # Import OpenCV for contour detection

ROOT_DIR = 'D:/AIM-LAB/BCC/after_mark/seven'
IMAGE_DIR = os.path.join(ROOT_DIR, "original-2")
ANNOTATION_DIR = os.path.join(ROOT_DIR, "mask/arborizing vessels-2")
ANNOTATION_DIR2 = os.path.join(ROOT_DIR, "mask/blue-grey globules-2")
ANNOTATION_DIR3 = os.path.join(ROOT_DIR, "mask/blue-grey ovoid nests-2")
ANNOTATION_DIR4 = os.path.join(ROOT_DIR, "mask/shiny white structures-2")
ANNOTATION_DIR5 = os.path.join(ROOT_DIR, "mask/ulceration-2")

INFO = {
    "description": "",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "",
    "year": 2017,
    "contributor": "",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]

# Customize based on your dataset
CATEGORIES = [
    {
        'id': 1,
        'name': 'arborizing vessels',
        'supercategory': 'arborizing vessels',
    },
    {
        'id': 2,
        'name': 'blue-grey globules',
        'supercategory': 'blue-grey globules',
    },
    {
        'id': 3,
        'name': 'blue-grey ovoid nests',
        'supercategory': 'blue-grey ovoid nests',
    },
    {
        'id': 4,
        'name': 'shiny white structures',
        'supercategory': 'shiny white structures',
    },
    {
        'id': 5,
        'name': 'ulceration',
        'supercategory': 'ulceration',
    }

]

def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg', '*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    return files

def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]
    return files

def count_contours(binary_mask):
    # Use OpenCV to find contours in the binary mask
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)


def main():
    coco_output = {
        "info": INFO,
        "licenses": LICENSES,
        "categories": CATEGORIES,
        "images": [],
        "annotations": []
    }

    image_id = 1
    segmentation_id = 1

    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        image_files = filter_for_jpeg(root, files)

        # go through each image
        for image_filename in image_files:
            image = Image.open(image_filename)
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)

            # Iterate over each annotation directory
            for annotation_dir in [ANNOTATION_DIR, ANNOTATION_DIR2, ANNOTATION_DIR3, ANNOTATION_DIR4, ANNOTATION_DIR5]:
                annotation_files = filter_for_annotations(annotation_dir, os.listdir(annotation_dir), image_filename)

                # go through each associated annotation
                for annotation_filename in annotation_files:
                    print(annotation_filename)
                    class_id = [x['id'] for x in CATEGORIES if x['name'] in annotation_filename][0]

                    category_info = {'id': class_id, 'is_crowd': 'crowd' in image_filename}
                    binary_mask = np.asarray(Image.open(annotation_filename)
                                             .convert('1')).astype(np.uint8)

                    annotation_info = pycococreatortools.create_annotation_info(
                        segmentation_id, image_id, category_info, binary_mask,
                        image.size, tolerance=2)

                    if annotation_info is not None:
                        coco_output["annotations"].append(annotation_info)

                    segmentation_id = segmentation_id + 1

            image_id = image_id + 1

    with open('{}/val_five.json'.format(ROOT_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)



if __name__ == "__main__":
    main()
