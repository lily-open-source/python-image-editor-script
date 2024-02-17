from PIL import Image
import os
from tkinter import filedialog
from tkinter import Tk

def resize_image(input_path, output_path, max_size=450, max_file_size_kb=512):
    try:
        with Image.open(input_path) as img:
            # Resize the image
            img.thumbnail((max_size, max_size))

            # Save the resized image
            img.save(output_path, quality=85)  # You can adjust the quality as needed

            # Check and adjust file size
            while os.path.getsize(output_path) > max_file_size_kb * 1024:
                img.save(output_path, quality=img.info['quality'] - 5)

            print(f"Image resized successfully: {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

def batch_resize_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # If source and output are the same, overwrite the source file
        if input_folder == output_folder:
            output_path = input_path
        else:
            output_path = os.path.join(output_folder, filename)

        # Resize only if it's an image file
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.raw', '.heif', '.heic', '.ico')):
            resize_image(input_path, output_path)

def main():
    root = Tk()
    root.withdraw()

    # Ask for the source folder containing images
    source_folder = filedialog.askdirectory(title="Select Source Folder")

    if source_folder:
        # Ask for the output folder to save resized images
        output_folder = filedialog.askdirectory(title="Select Output Folder")

        if output_folder:
            batch_resize_images(source_folder, output_folder)
            print("Image resize process completed.")
        else:
            print("No output folder selected. Exiting.")
    else:
        print("No source folder selected. Exiting.")

if __name__ == "__main__":
    main()
