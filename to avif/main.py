import os
import subprocess
from tkinter import filedialog
from tkinter import Tk

def compress_image(input_path, output_path):
    """
    Compresses an image to AVIF format using avifenc command-line tool.

    Parameters:
    - input_path: Path to the input image file.
    - output_path: Path to save the compressed image.
    """
    try:
        subprocess.run(['avifenc', input_path, '-o', output_path, '--min', '8', '--max', '63', '--speed', '0'])
        print(f"Compression successful: {output_path}")
    except Exception as e:
        print(f"Error compressing image: {e}")

def batch_compress_images(input_folder):
    """
    Batch compresses images in a folder to AVIF format.

    Parameters:
    - input_folder: Folder containing input images.
    """
    output_folder = os.path.join(input_folder, 'out')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.raw', '.heif', '.heic', '.ico')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename.split('.')[0]}_compressed.avif")
            compress_image(input_path, output_path)

def main():
    root = Tk()
    root.withdraw()

    # Ask for the source folder containing images
    source_folder = filedialog.askdirectory(title="Select Source Folder")

    if source_folder:
        batch_compress_images(source_folder)
        print("Image compression process completed.")
    else:
        print("No source folder selected. Exiting.")

if __name__ == "__main__":
    main()
