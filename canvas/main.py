from PIL import Image
import os
from tkinter import Tk, simpledialog, filedialog, Button

canvas_option = None
scale_factor = None
custom_size = None

def resize_canvas_auto(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Determine the new canvas size (square)
            max_dimension = max(img.width, img.height)
            new_size = (max_dimension, max_dimension)

            # Create a new image with the adjusted canvas size
            new_img = Image.new("RGBA", new_size, (255, 255, 255, 0))

            # Paste the original image onto the new canvas
            new_img.paste(img, ((max_dimension - img.width) // 2, (max_dimension - img.height) // 2))

            # Save the image with the adjusted canvas size
            new_img.save(output_path)
            print(f"Canvas resized successfully: {output_path}")
    except Exception as e:
        print(f"Error resizing canvas: {e}")

def resize_canvas_rescale(input_path, output_path, scale_factor):
    try:
        with Image.open(input_path) as img:
            # Calculate the new canvas size using the scale factor
            new_size = (int(img.width * scale_factor), int(img.height * scale_factor))

            # Create a new image with the adjusted canvas size
            new_img = Image.new("RGBA", new_size, (255, 255, 255, 0))

            # Resize the original image elements based on the scale factor
            img_resized = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)))

            # Paste the resized original image onto the new canvas
            new_img.paste(img_resized, ((new_size[0] - img_resized.width) // 2, (new_size[1] - img_resized.height) // 2))

            # Save the image with the adjusted canvas size
            new_img.save(output_path)
            print(f"Canvas and image elements resized successfully: {output_path}")
    except Exception as e:
        print(f"Error resizing canvas: {e}")

def resize_canvas_custom(input_path, output_path, custom_size):
    try:
        with Image.open(input_path) as img:
            # Create a new image with the custom canvas size
            new_img = Image.new("RGBA", (custom_size, custom_size), (255, 255, 255, 0))

            # Paste the original image onto the new canvas
            new_img.paste(img, ((custom_size - img.width) // 2, (custom_size - img.height) // 2))

            # Save the image with the adjusted canvas size
            new_img.save(output_path)
            print(f"Canvas resized successfully: {output_path}")
    except Exception as e:
        print(f"Error resizing canvas: {e}")

def single_option():
    global canvas_option
    canvas_option = simpledialog.askstring("Canvas Size Option", "Enter 'auto', 'rescale', or 'custom' for canvas size:")

    if canvas_option and canvas_option.lower() in ['auto', 'rescale', 'custom']:
        source_file = filedialog.askopenfilename(title="Select Source File")

        if source_file:
            output_folder = filedialog.askdirectory(title="Select Output Folder")

            if output_folder:
                if canvas_option.lower() == 'auto':
                    resize_canvas_auto(source_file, os.path.join(output_folder, os.path.basename(source_file)))
                elif canvas_option.lower() == 'rescale':
                    global scale_factor
                    scale_factor_str = simpledialog.askstring("Scale Factor", "Enter the scale factor (e.g., 2 for doubling size, 0.5 for halving size):")

                    if scale_factor_str:
                        try:
                            scale_factor = float(scale_factor_str)
                            resize_canvas_rescale(source_file, os.path.join(output_folder, os.path.basename(source_file)), scale_factor)
                        except (ValueError, TypeError) as e:
                            print(f"Invalid input: {e}. Exiting.")
                    else:
                        print("No scale factor entered. Exiting.")
                elif canvas_option.lower() == 'custom':
                    global custom_size
                    custom_size_str = simpledialog.askstring("Custom Size", "Enter the custom size (e.g., enter '800' for both width and height):")

                    if custom_size_str:
                        try:
                            custom_size = int(custom_size_str)
                            resize_canvas_custom(source_file, os.path.join(output_folder, os.path.basename(source_file)), custom_size)
                        except (ValueError, TypeError) as e:
                            print(f"Invalid input: {e}. Exiting.")
                    else:
                        print("No custom size entered. Exiting.")
                print("Canvas and image elements resize process completed.")
            else:
                print("No output folder selected. Exiting.")
        else:
            print("No source file selected. Exiting.")
    else:
        print("Invalid canvas size option selected. Exiting.")

def batch_resize_canvas(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # If output folder does not exist, create it
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # If source and output are the same, overwrite the source file
        if input_folder == output_folder:
            output_path = input_path
        else:
            output_path = os.path.join(output_folder, filename)

        # Resize canvas and image elements based on the selected option
        if canvas_option.lower() == 'auto':
            resize_canvas_auto(input_path, output_path)
        elif canvas_option.lower() == 'rescale':
            resize_canvas_rescale(input_path, output_path, scale_factor)
        elif canvas_option.lower() == 'custom':
            resize_canvas_custom(input_path, output_path, custom_size)

def multiple_option():
    global canvas_option
    canvas_option = simpledialog.askstring("Canvas Size Option", "Enter 'auto', 'rescale', or 'custom' for canvas size:")

    if canvas_option and canvas_option.lower() in ['auto', 'rescale', 'custom']:
        source_folder = filedialog.askdirectory(title="Select Source Folder")

        if source_folder:
            output_folder = filedialog.askdirectory(title="Select Output Folder")

            if output_folder:
                batch_resize_canvas(source_folder, output_folder)
                print("Canvas and image elements resize process completed.")
            else:
                print("No output folder selected. Exiting.")
        else:
            print("No source folder selected. Exiting.")
    else:
        print("Invalid canvas size option selected. Exiting.")

def main():
    root = Tk()
    root.withdraw()

    single_button = Button(root, text="Single", command=single_option)
    single_button.pack(pady=10)

    multiple_button = Button(root, text="Multiple", command=multiple_option)
    multiple_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
