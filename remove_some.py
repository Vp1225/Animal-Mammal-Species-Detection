import shutil
import os

# Main directory containing the folders you want to delete
main_folder = "test"

# List of folder names to delete
folders_to_delete = [
    "african_elephant", "alpaca", "american_bison", "anteater", "arctic_fox",
    "armadillo", "baboon", "badger", "blue_whale", "brown_bear", "camel",
    "dolphin", "giraffe", "groundhog", "highland_cattle", "horse", "jackal",
    "kangaroo", "koala", "manatee", "mongoose", "mountain_goat", "opossum",
    "orangutan", "otter", "polar_bear", "porcupine", "red_panda", "rhinoceros",
    "sea_lion", "seal", "snow_leopard", "squirrel", "sugar_glider", "tapir",
    "vampire_bat", "vicuna", "walrus", "warthog", "water_buffalo", "weasel",
    "wildebeest", "wombat", "yak", "zebra"
]

# Deleting each specified folder within the main folder
for folder in folders_to_delete:
    folder_path = os.path.join(main_folder, folder)
    try:
        shutil.rmtree(folder_path)
        print(f"'{folder}' has been successfully deleted from '{main_folder}'.")
    except Exception as e:
        print(f"Error deleting '{folder}': {e}")

