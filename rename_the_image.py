import os

def rename_images(folder_path):
    # Check if the specified folder path exists
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        return
    
    # Get the list of images in the specified folder
    images = [image for image in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, image))]
    
    # Initialize counting number
    count = 1
    
    # Rename each image in the specified folder
    for image_name in images:
        # Get the file extension
        _, extension = os.path.splitext(image_name)
        
        # Construct the new image name
        new_image_name = f"{os.path.basename(folder_path)}-{count:04}{extension}"
        
        # Rename the image
        old_image_path = os.path.join(folder_path, image_name)
        new_image_path = os.path.join(folder_path, new_image_name)
        os.rename(old_image_path, new_image_path)
        
        # Increment counting number
        count += 1

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder containing images: ")
    rename_images(folder_path)
