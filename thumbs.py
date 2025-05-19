import os

from PIL import Image

input_dir = "building"
output_dir = "thumbs"
i = -1
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.png')):
        img = Image.open(f"{input_dir}/{filename}")
        # 调整尺寸并转换格式
        img.thumbnail((800, 800))
        i = i + 1
        base_name = str(i).zfill(3)
        img.save(f"{output_dir}/{base_name}.webp", "WEBP", quality=80)