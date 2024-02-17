# Image Resize (downsize) Script

## Overview

This Python script is designed to resize images to a maximum of 450 pixels in height or width and ensure the file size is under 512 KB. The script includes a basic UI using the tkinter library, allowing users to select the source and output folders. If the source and output folders are the same, the script will automatically overwrite the source files with the processed ones.

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)

## Workflow

1. **Install Dependencies:**
   - Make sure you have Python 3.x installed.
   - Install the Pillow library by running:

     ```bash
     pip install Pillow
     ```

2. **Run the Script:**
   - Execute the script by running the following command in your terminal or command prompt:

     ```bash
     python downsize.py
     ```

3. **Select Source and Output Folders:**
   - The script will open two UI dialogs prompting you to select the source and output folders. Choose the folders accordingly.

4. **Resize Process:**
   - The script will resize images in the selected source folder to a maximum of 450 pixels in height or width and ensure the file size is under 512 KB. If the source and output folders are the same, the script will automatically overwrite the source files with the processed ones.

5. **Completion:**
   - Once the process is complete, the script will print a message indicating that the image resize is finished.

## Note

- This script assumes that your images are in common formats like JPG, JPEG, PNG, GIF, BMP, TIFF, TIF, WebP, SVG, RAW, HEIF, HEIC, or ICO. Adjust the file extensions in the `endswith` check if needed.

- If the source and output folders are the same, the script will automatically overwrite the source files with the processed ones.

- In case of any errors during the resize process, the script will print an error message with details.

## Disclaimer

Use this script responsibly. Image resizing may result in a loss of quality, and it's important to consider the trade-off between file size and image quality for your specific use case.

Feel free to customize the script or contribute improvements. If you encounter any issues or have suggestions, please open an issue or submit a pull request.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Workflow](#workflow)
   - [Install Dependencies](#1-install-dependencies)
   - [Run the Script](#2-run-the-script)
   - [Select Source and Output Folders](#3-select-source-and-output-folders)
   - [Resize Process](#4-resize-process)
   - [Completion](#5-completion)
4. [Note](#note)
5. [Disclaimer](#disclaimer)
6. [Table of Contents](#table-of-contents)

