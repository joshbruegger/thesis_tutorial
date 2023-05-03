import os
from PIL import Image


def max_image_size(folder_path):
    max_width, max_height = 0, 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        try:
            with Image.open(file_path) as img:
                width, height = img.size

                if width > max_width:
                    max_width = width

                if height > max_height:
                    max_height = height

        except IOError:
            print(f"{filename} is not an image file or could not be opened.")

    return max_width, max_height


if __name__ == "__main__":
    folder_path = input(
        "Enter the folder path containing the images: ").strip()

    if os.path.isdir(folder_path):
        max_width, max_height = max_image_size(folder_path)
        print(
            f"The maximum image size in the folder is {max_width}x{max_height} pixels.")
    else:
        print("Invalid folder path. Please try again.")
