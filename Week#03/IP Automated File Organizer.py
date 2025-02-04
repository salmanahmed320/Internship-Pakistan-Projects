# INTERNSHIP PAKISTAN
# WEEK 3 : File Handling And Basic Automation 
# Task #2: Automated File Organizer
# Create a script that organizes files in a directory into folders based on their file types (e.g., images, documents).
        
from pathlib import Path
# Define the directory to organize
directory = Path(input("Enter the directory path: "))
# Define file type categories and their corresponding folder names
categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Others': []
}
# Iterate through the files in the directory
for file in directory.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        # Determine the target folder based on file extension
        target_folder = 'Others'
        for folder, extensions in categories.items():
            if ext in extensions:
                target_folder = folder
                break
        # Create the target folder if it doesn't exist
        target_path = directory / target_folder
        target_path.mkdir(exist_ok=True)
        # Move the file to the target folder
        file.rename(target_path / file.name)
        print(f"Moved {file.name} to {target_folder}/")
