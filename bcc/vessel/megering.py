# from skimage import data
# from skimage import color
# from skimage.filters import meijering, sato, frangi, hessian
# import matplotlib.pyplot as plt
#
#
# def original(image, **kwargs):
#     """Return the original image, ignoring any kwargs."""
#     return image
#
#
# image = color.rgb2gray(data.retina())[300:700, 700:900]
# cmap = plt.cm.gray
#
# plt.rcParams["axes.titlesize"] = "medium"
# axes = plt.figure(figsize=(10, 4)).subplots(2, 9)
# for i, black_ridges in enumerate([True, False]):
#     for j, (func, sigmas) in enumerate([
#             (original, None),
#             (meijering, [1]),
#             (meijering, range(1, 5)),
#             (sato, [1]),
#             (sato, range(1, 5)),
#             (frangi, [1]),
#             (frangi, range(1, 5)),
#             (hessian, [1]),
#             (hessian, range(1, 5)),
#     ]):
#         result = func(image, black_ridges=black_ridges, sigmas=sigmas)
#         axes[i, j].imshow(result, cmap=cmap)
#         if i == 0:
#             title = func.__name__
#             if sigmas:
#                 title += f"\n\N{GREEK SMALL LETTER SIGMA} = {list(sigmas)}"
#             axes[i, j].set_title(title)
#         if j == 0:
#             axes[i, j].set_ylabel(f'{black_ridges = }')
#         axes[i, j].set_xticks([])
#         axes[i, j].set_yticks([])
#
# plt.tight_layout()
# plt.show()

import os
from skimage import io, color
from skimage.filters import meijering, sato, frangi, hessian
from skimage import img_as_ubyte
import matplotlib.pyplot as plt

def process_and_save(image_path, output_path, black_ridges, func, sigmas=None):
    """Process the image, save the result with a specific suffix."""
    image = color.rgb2gray(io.imread(image_path))
    result = func(image, black_ridges=black_ridges, sigmas=sigmas)
    result = img_as_ubyte(result)  # Convert to 8-bit unsigned integer

    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(image_path))[0]

    # Construct the output filename with the original name and feature-related suffix
    output_filename = f"{base_filename}_{func.__name__}_{'black' if black_ridges else 'white'}"
    if sigmas:
        output_filename += f"_sigma_{sigmas}"
    output_filename += ".png"
    output_filepath = os.path.join(output_path, output_filename)
    io.imsave(output_filepath, result)

def process_images(input_path, output_path):
    """Process images from the input path and save results in the output path."""
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(input_path, image_file)
        for black_ridges in [True, False]:
            for func, sigmas in [
                (meijering, [1]),
                (meijering, list(range(1, 5))),
                # (sato, [1]),
                # (sato, list(range(1, 5))),
                # (frangi, [1]),
                # (frangi, list(range(1, 5))),
                # (hessian, [1]),
                # (hessian, list(range(1, 5))),
            ]:
                process_and_save(image_path, output_path, black_ridges, func, sigmas)

if __name__ == "__main__":
    input_path = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\arborizing vessels orin train"
    output_path = "D:\\AIM-LAB\\BCC\\after_mark\\seven\\mask\\arborizing vessels orin train test"

    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    process_images(input_path, output_path)
