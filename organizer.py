# Intern ID: CITS9867
# Task 1: Automated File Organizer - Codtech Internship

import os
import shutil

def organize_files(folder_path):
    # File types mapping
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Python': ['.py']
    }

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} -> {folder_name}")
                    break
    
    print("\nOrganization Complete!")

# For testing - Create a test folder
path = input("Enter folder path to organize (or press Enter for current folder): ").strip()
if path == "":
    path = os.getcwd()

organize_files(path)
