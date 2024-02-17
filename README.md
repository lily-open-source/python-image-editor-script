# python-image-editor-script

## Image Recale Script

This Python script provides a flexible image resizing solution. It allows users to resize a single image or batch resize multiple images in a folder. The script utilizes the `Pillow` library and includes a basic UI using the `tkinter` library for user interaction.

- [code](rescale)

## Image Resize (downsize) Script

This Python script is designed to resize images to a maximum of 450 pixels in height or width and ensure the file size is under 512 KB. The script includes a basic UI using the tkinter library, allowing users to select the source and output folders. If the source and output folders are the same, the script will automatically overwrite the source files with the processed ones.

- [code](downsize)

## Image Metadata Removal Script

This Python script is designed to remove metadata, also known as EXIF data, from images in a specified folder. Metadata often includes information about the camera settings, date and time the photo was taken, and other details. By running this script, you can automate the process of stripping metadata from multiple images, reducing their file sizes.

- [code](metadata)

## Image Canvas Resizer

This Python script provides a simple GUI for resizing the canvas of PNG files. It allows users to choose between processing a single file or multiple files in a folder. The script uses the PIL (Pillow) library for image processing.

- [code](canvas)

## Image Compression Script (image to avif)

This Python script is designed to compress images to the AVIF format using the avifenc command-line tool. The script includes a basic UI using the tkinter library, allowing users to select the source folder containing their images. The compressed images are saved in an 'out' folder within the source directory.

- [code](to-avif)
