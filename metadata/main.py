import os
from tkinter import filedialog
from tkinter import Tk
from PIL import Image, ExifTags

def remove_metadata(image_path):
    try:
        image = Image.open(image_path)
        # Remove EXIF data
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        # Save the image without metadata
        image_without_exif.save(image_path)
        print(f"Metadata removed from {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            remove_metadata(image_path)

def main():
    root = Tk()
    root.withdraw()

    # Ask for the folder containing images
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")

    if folder_path:
        process_images_in_folder(folder_path)
        print("Metadata removal process completed.")
    else:
        print("No folder selected. Exiting.")

if __name__ == "__main__":
    main()

