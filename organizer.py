import os
import shutil

# File extensions and their destination folders
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
}

def get_category(extension):
    for category, extensions in file_categories.items():
        if extension.lower() in extensions:
            return category
    return None


def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: The folder does not exist.")
        return

    moved_count = 0

    try:
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if not entry.is_file():
                    continue

                extension = os.path.splitext(entry.name)[1]
                category = get_category(extension)

                if category is None:
                    continue

                destination_folder = os.path.join(folder_path, category)
                os.makedirs(destination_folder, exist_ok=True)

                destination_path = os.path.join(
                    destination_folder, entry.name
                )

                # Avoid overwriting files with the same name
                if os.path.exists(destination_path):
                    name, ext = os.path.splitext(entry.name)
                    counter = 1

                    while os.path.exists(destination_path):
                        new_name = f"{name}_{counter}{ext}"
                        destination_path = os.path.join(
                            destination_folder, new_name
                        )
                        counter += 1

                shutil.move(entry.path, destination_path)
                print(f"Moved: {entry.name} -> {category}")
                moved_count += 1

        print(f"\nOrganization completed!")
        print(f"Total files moved: {moved_count}")

    except PermissionError:
        print("Error: Permission denied. Check folder permissions.")
    except OSError as error:
        print(f"An error occurred: {error}")


# Main program
print("===== FILE ORGANIZER =====")
folder = input("Enter the folder path to organize: ").strip().strip('"')

organize_files(folder)