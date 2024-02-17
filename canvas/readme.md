# Image Canvas Resizer

## Overview

This Python script provides a simple GUI for resizing the canvas of PNG files. It allows users to choose between processing a single file or multiple files in a folder. The script uses the PIL (Pillow) library for image processing.

## Features

- **Canvas Size Options:**
  - **Auto:** Resizes the canvas to be square, using the maximum of the original width and height.
  - **Rescale:** Prompts the user for a scale factor to adjust both the canvas and image elements.
  - **Custom:** Prompts the user for a desire resolution to adjust both the canvas and image elements.

- **User Interaction:**
  - The script prompts users to select the file type ('single' or 'multiple') and canvas size option.
  - For the 'rescale' option, users enter a scale factor for adjusting the canvas and image elements.

- **File Handling:**
  - The script creates an output folder for the resized images if it doesn't exist.
  - If the source and output folders are the same, the script overwrites the source files with the processed ones.

## Requirements

- Python 3.x
- Pillow library (install using `pip install pillow`)

## Usage

1. Run the script by executing the command: `python main.py`
2. Select the file type ('single' or 'multiple').
3. Choose the canvas size option ('auto','rescale', or 'custom').
4. If 'rescale' is selected, enter the scale factor when prompted.
5. If 'custom' is selected, enter the desire resolution when prompted.
6. Select the source file or folder.
7. Choose the output folder for saving the resized images.
8. The script will process the images based on the selected options.

## Note

- Ensure that the Pillow library is installed before running the script.

- If the source and output folders are the same, the script will automatically overwrite the source files with the processed ones.

- In case of any errors during the resize process, the script will print an error message with details.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Note](#note)
6. [Table of Contents](#table-of-contents)
