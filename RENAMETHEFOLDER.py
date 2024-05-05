import os
import re
import sys

def rename_subfolders(folder_path):
    # Check if the specified folder path exists
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        return
    
    # Get the list of subfolders in the specified folder
    subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]
    
    # Define regular expression pattern to match typographical symbols and underscores
    pattern = r'[^\w\s_]'
    
    for subfolder in subfolders:
        # Rename only if the subfolder name starts with a lowercase letter
        if subfolder[0].islower():
            # Capitalize the first letter of the subfolder name
            new_name = subfolder.capitalize()
            
            # Remove typographical symbols and underscores from the subfolder name
            new_name = re.sub(pattern, '', new_name)
            
            # Check if the new name is different from the old one
            if new_name != subfolder:
                # Rename the subfolder
                old_path = os.path.join(folder_path, subfolder)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed '{subfolder}' to '{new_name}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    rename_subfolders(folder_path)
