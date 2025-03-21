import os
from rembg import remove
from PIL import Image

def remove_background(input_dir="input", output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".jpg"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, f"{file_name[:-4]}_bg.png")

            try:
                input_image = Image.open(input_path)
                output_image = remove(input_image)
                output_image.save(output_path)
                print(f"Processed {file_name} -> {output_path}")

            except Exception as e:
                print(f"Error processing {file_name}: {e}")
