
import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Others": []
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            new_path = os.path.join(category_folder, filename)
            shutil.move(file_path, new_path)
            print(f"Moved: {filename} --> {category}/")

    print("\nFiles organized successfully.")

def main():
    folder_path = input("Enter the folder path to organize: ").strip()
    organize_folder(folder_path)

if __name__ == "__main__":
    main()
