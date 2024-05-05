import os
import shutil
from sklearn.model_selection import train_test_split

# Dataset location
dataset_path = r'C:\Users\ADMIN\Desktop\backup - backup\Animal(mammal) species detection\mammals'
train_dir = os.path.join(dataset_path, 'train')
val_dir = os.path.join(dataset_path, 'validation')
test_dir = os.path.join(dataset_path, 'test')

for dir in [train_dir, val_dir, test_dir]:
    if not os.path.exists(dir):
        os.makedirs(dir)

test_size = 0.20
val_size = 0.25

for class_name in os.listdir(dataset_path):
    class_dir = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_dir):
        filenames = os.listdir(class_dir)
        filenames = [os.path.join(class_dir, f) for f in filenames if f.lower().endswith(('png', 'jpg', 'jpeg'))]

        if not filenames:
            print(f"No image files found in {class_dir}. Skipping...")
            continue

        train_and_val, test_filenames = train_test_split(filenames, test_size=test_size, random_state=42)
        train_filenames, val_filenames = train_test_split(train_and_val, test_size=val_size, random_state=42)

        def copy_files(files, dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
            for f in files:
                shutil.copy(f, dest_dir)

        copy_files(train_filenames, os.path.join(train_dir, class_name))
        copy_files(val_filenames, os.path.join(val_dir, class_name))
        copy_files(test_filenames, os.path.join(test_dir, class_name))
