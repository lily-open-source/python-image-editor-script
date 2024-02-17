from PIL import Image
import os
from tkinter import simpledialog, filedialog, Tk, Label, Button

def resize_image(input_path, output_path, scale_factor, quality):
    try:
        with Image.open(input_path) as img:
            # Resize the image
            new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
            resized_img = img.resize(new_size)

            # Save the resized image
            resized_img.save(output_path, quality=quality)
            print(f"Image resized successfully: {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

def batch_resize_images(input_folder, output_folder, scale_factor, quality):
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # If source and output are the same, overwrite the source file
        if input_folder == output_folder:
            output_path = input_path
        else:
            output_path = os.path.join(output_folder, filename)

        # Resize only if it's an image file
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.raw', '.heif', '.heic', '.ico')):
            resize_image(input_path, output_path, scale_factor, quality)

def main():
    root = Tk()
    root.title("Image Resizer")

    def choose_single_file():
        source_file = filedialog.askopenfilename(title="Select Source File")
        if source_file:
            output_folder = filedialog.askdirectory(title="Select Output Folder")
            if output_folder:
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                scale_factor_str = simpledialog.askstring("Scaling Factor", "Enter the scaling factor (e.g., 2 for doubling size, -0.5 for halving size):")
                if scale_factor_str:
                    quality_str = simpledialog.askstring("Quality", "Enter the quality (0-100, higher is better):")
                    if quality_str:
                        try:
                            scale_factor = float(scale_factor_str)
                            quality = int(quality_str)
                            resize_image(source_file, os.path.join(output_folder, os.path.basename(source_file)), scale_factor, quality)
                            print("Image resize process completed.")
                        except (ValueError, TypeError) as e:
                            print(f"Invalid input: {e}. Exiting.")
                    else:
                        print("No quality entered. Exiting.")
                else:
                    print("No scaling factor entered. Exiting.")
            else:
                print("No output folder selected. Exiting.")
        else:
            print("No source file selected. Exiting.")

    def choose_multiple_files():
        source_folder = filedialog.askdirectory(title="Select Source Folder")
        if source_folder:
            output_folder = filedialog.askdirectory(title="Select Output Folder")
            if output_folder:
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                scale_factor_str = simpledialog.askstring("Scaling Factor", "Enter the scaling factor (e.g., 2 for doubling size, -0.5 for halving size):")
                if scale_factor_str:
                    quality_str = simpledialog.askstring("Quality", "Enter the quality (0-100, higher is better):")
                    if quality_str:
                        try:
                            scale_factor = float(scale_factor_str)
                            quality = int(quality_str)
                            batch_resize_images(source_folder, output_folder, scale_factor, quality)
                            print("Image resize process completed.")
                        except (ValueError, TypeError) as e:
                            print(f"Invalid input: {e}. Exiting.")
                    else:
                        print("No quality entered. Exiting.")
                else:
                    print("No scaling factor entered. Exiting.")
            else:
                print("No output folder selected. Exiting.")
        else:
            print("No source folder selected. Exiting.")

    single_file_button = Button(root, text="Choose Single File", command=choose_single_file)
    single_file_button.pack()

    multiple_files_button = Button(root, text="Choose Multiple Files", command=choose_multiple_files)
    multiple_files_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
