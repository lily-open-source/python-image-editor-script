# Image Compression Script (image to avif)

## Overview

This Python script is designed to compress images to the AVIF format using the avifenc command-line tool. The script includes a basic UI using the tkinter library, allowing users to select the source folder containing their images. The compressed images are saved in an 'out' folder within the source directory.

## Requirements

- Python 3.x
- avifenc command-line tool (Install from [libavif](https://github.com/AOMediaCodec/libavif))
- tkinter library (`pip install tk`)

## Workflow

1. **Install Dependencies:**
   - Make sure you have Python 3.x installed.
   - Install the avifenc command-line tool from [libavif](https://github.com/AOMediaCodec/libavif).
   - Install the tkinter library by running:

     ```bash
     pip install tk
     ```

2. **Run the Script:**
   - Execute the script by running the following command in your terminal or command prompt:

     ```bash
     python image_to_avif.py
     ```

3. **Select Source Folder:**
   - The script will open a UI dialog prompting you to select the source folder containing your images. Use the provided file dialog to choose the target folder.

4. **Compression:**
   - The script will batch compress images in the selected folder to the AVIF format using the avifenc command-line tool.

5. **Completion:**
   - Once the process is complete, the script will print a message indicating that the image compression is finished.

## Note

- This script assumes that your images are in common formats like JPG, JPEG, PNG, GIF, BMP, TIFF, TIF, WebP, SVG, RAW, HEIF, HEIC, or ICO. Adjust the file extensions in the `endswith` check if needed.

- The compressed images are saved in an 'out' folder within the selected source directory.

- In case of any errors during compression, the script will print an error message with details.

## Disclaimer

Use this script responsibly. Image compression may result in a loss of quality, and it's important to consider the trade-off between file size and image quality for your specific use case.

Feel free to customize the script or contribute improvements. If you encounter any issues or have suggestions, please open an issue or submit a pull request.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Workflow](#workflow)
   - [Install Dependencies](#1-install-dependencies)
   - [Run the Script](#2-run-the-script)
   - [Select Source Folder](#3-select-source-folder)
   - [Compression](#4-compression)
   - [Completion](#5-completion)
4. [Note](#note)
5. [Disclaimer](#disclaimer)
6. [Table of Contents](#table-of-contents)
