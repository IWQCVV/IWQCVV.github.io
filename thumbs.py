import os

from PIL import Image

input_dir = "photos/Meeting_photos"
output_dir = "thumbs"
i = 4
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.png')):
        img = Image.open(f"{input_dir}/{filename}")
        # 调整尺寸并转换格式
        img.thumbnail((800, 800))
        i = i + 1
        base_name = str(i).zfill(3)
        img.save(f"{output_dir}/{base_name}.webp", "WEBP", quality=80)