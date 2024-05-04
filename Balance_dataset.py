import os
from PIL import Image, ImageOps
import glob

def augment_image(image_path, output_dir):
    """Apply augmentation to a single image and save the new images."""
    image = Image.open(image_path)
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)

    original_path = os.path.join(output_dir, f"{name}_original{ext}")
    image.save(original_path)

    lr_flipped = ImageOps.mirror(image)
    lr_path = os.path.join(output_dir, f"{name}_lr{ext}")
    lr_flipped.save(lr_path)

    ud_flipped = ImageOps.flip(image)
    ud_path = os.path.join(output_dir, f"{name}_ud{ext}")
    ud_flipped.save(ud_path)

    rotated_90 = image.rotate(90)
    rot_90_path = os.path.join(output_dir, f"{name}_rot90{ext}")
    rotated_90.save(rot_90_path)

    rotated_180 = image.rotate(180)
    rot_180_path = os.path.join(output_dir, f"{name}_rot180{ext}")
    rotated_180.save(rot_180_path)

    rotated_270 = image.rotate(270)
    rot_270_path = os.path.join(output_dir, f"{name}_rot270{ext}")
    rotated_270.save(rot_270_path)

def augment_folder(folder_path, limit=350):
    """Augment all images in a folder until reaching the specified limit."""
    images = glob.glob(os.path.join(folder_path, "*.jpg"))  
    count = len(images)
    idx = 0
    while count < limit and idx < len(images):
        augment_image(images[idx], folder_path)
        count = len(glob.glob(os.path.join(folder_path, "*.jpg")))
        idx += 1

def main():
    dataset_dir = r"C:\Users\ADMIN\Desktop\backup - backup\Animal(mammal) species detection\mammals"
    species_folders = [os.path.join(dataset_dir, folder) for folder in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, folder))]

    for folder in species_folders:
        print(f"Augmenting images in {folder}...")
        augment_folder(folder)

if __name__ == "__main__":
    main()
