# rename photos name to numbers from 001 to 999


import os
import re
import shutil


def rename_photos(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the input directory
    files = os.listdir(input_dir)

    # Filter out non-image files
    image_files = [f for f in files if re.match(r'.*\.(jpg|jpeg|png|webp)$', f, re.IGNORECASE)]


    # Rename and copy the images to the output directory
    for i, filename in enumerate(image_files, start=1):
        new_name = f"{str(i+4).zfill(3)}.webp"
        shutil.copy(os.path.join(input_dir, filename), os.path.join(output_dir, new_name))

if __name__ == "__main__":
    input_dir = "photos/Meeting_photos"
    output_dir = "renamed_photos"
    rename_photos(input_dir, output_dir)