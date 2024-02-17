# Image Resize Script

## Overview

This Python script provides a flexible image resizing solution. It allows users to resize a single image or batch resize multiple images in a folder. The script utilizes the `Pillow` library and includes a basic UI using the `tkinter` library for user interaction.

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
     python main.py
     ```

3. **Select Single File or Multiple Files:**
   - The script will prompt you to choose whether you want to resize a single file or multiple files in a folder.

4. **If Resizing a Single File:**
   - The script will then ask you to select the source image file.
   - Next, you will specify the output folder to save the resized image.
   - Enter the scaling factor (e.g., 2 for doubling size, -0.5 for halving size).
   - Enter the quality (0-100, higher is better).
   - The resized image will be saved in the specified output folder.

5. **If Resizing Multiple Files:**
   - The script will prompt you to select the source folder containing multiple images.
   - Specify the output folder to save the resized images.
   - Enter the scaling factor (e.g., 2 for doubling size, -0.5 for halving size).
   - Enter the quality (0-100, higher is better).
   - The batch resizing process will be completed, and resized images will be saved in the output folder.

6. **Note:**
   - The script accepts negative values for the scaling factor, allowing users to downscale images as well.
   - Adjust the `quality` parameter in the `save` method as needed.

7. **Disclaimer:**
   - Use this script responsibly. Image resizing may result in a loss of quality, and it's essential to consider the trade-off between file size and image quality for your specific use case.

8. **Customization and Contributions:**
   - Feel free to customize the script or contribute improvements.
   - If you encounter any issues or have suggestions, please open an issue or submit a pull request.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Workflow](#workflow)
   - [Install Dependencies](#1-install-dependencies)
   - [Run the Script](#2-run-the-script)
   - [Select Single File or Multiple Files](#3-select-single-file-or-multiple-files)
   - [If Resizing a Single File](#4-if-resizing-a-single-file)
   - [If Resizing Multiple Files](#5-if-resizing-multiple-files)
   - [Note](#6-note)
   - [Disclaimer](#7-disclaimer)
   - [Customization and Contributions](#8-customization-and-contributions)
9. [Table of Contents](#table-of-contents)
