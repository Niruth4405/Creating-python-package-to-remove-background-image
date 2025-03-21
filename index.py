import os
from rembg import remove
from PIL import Image

input_dir = "input/"
output_dir = "output/"

os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(input_dir):
    if file_name.endswith(".jpg"):
        input_path = os.path.join(input_dir, file_name)
        out_path = os.path.join(output_dir, f"{file_name[:-4]}_bg.png")

        try:
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(out_path)
            print(f"Processed {file_name} -> {out_path}")

        except Exception as e:
            print(f"An error occurred while processing {file_name}: {e}")
