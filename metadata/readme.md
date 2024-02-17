# Image Metadata Removal Script

## Overview

This Python script is designed to remove metadata, also known as EXIF data, from images in a specified folder. Metadata often includes information about the camera settings, date and time the photo was taken, and other details. By running this script, you can automate the process of stripping metadata from multiple images, reducing their file sizes.

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)

## Workflow

1. **Install Dependencies:**
   Make sure you have Python 3.x installed. Install the required Pillow library by running:

   ```bash
   pip install Pillow
   ```

2. **Run the Script:**
   Execute the script by running the following command in your terminal or command prompt:

   ```bash
   python Metadata_Removal.py
   ```

3. **Select Image Folder:**
   The script will prompt you to select the folder containing your images. Use the provided file dialog to choose the target folder.

4. **Processing:**
   The script will iterate through the images in the selected folder, removing their metadata and saving the modified images.

5. **Completion:**
   Once the process is complete, the script will print a message indicating that the metadata removal is finished.

## Note

- This script assumes that your images are in common formats like PNG, JPG, or JPEG. If your images have different file extensions, you may need to adjust the file extensions in the script accordingly.

- The script uses the Pillow library for image processing and the tkinter library for creating a basic terminal UI.

- In case of any errors during processing, the script will print an error message with details.

## Disclaimer

Use this script responsibly. Removing metadata means losing information about the image, and it's important to consider the implications of this trade-off for your specific use case.

Feel free to customize the script or contribute improvements. If you encounter any issues or have suggestions, please open an issue or submit a pull request.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Workflow](#workflow)
   - [Install Dependencies](#1-install-dependencies)
   - [Run the Script](#2-run-the-script)
   - [Select Image Folder](#3-select-image-folder)
   - [Processing](#4-processing)
   - [Completion](#5-completion)
4. [Note](#note)
5. [Disclaimer](#disclaimer)
6. [Table of Contents](#table-of-contents)
