import os
import shutil
from tkinter import Tk, Canvas, Button, filedialog, messagebox


def main():
    window = Tk()

    window.geometry("500x303")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=303,
        width=500,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        500.0,
        72.0,
        fill="#00FFA3",
        outline=""
    )

    canvas.create_text(
        50.0,
        11.0,
        anchor="nw",
        text="\nSort Your Files Fast",
        fill="#000000",
        font="Arial"
    )

    button_1 = Button(
        text="Select Directory",
        borderwidth=0,
        highlightthickness=0,
        command=gui_start,
        relief="flat"
    )
    button_1.place(
        x=114.0,
        y=117.0,
        width=293.0,
        height=33.0
    )

    canvas.create_text(
        0.0,
        281.0,
        anchor="nw",
        text="Created by: Antal Krisztian\n",
        fill="#000000",
        font=("Inter Medium", 12 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


def select_directory():
    """Prompt the user to select a directory."""
    user_path = filedialog.askdirectory(title='Select Folder')
    return user_path


def create_directory(new_folder):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        messagebox.showinfo("Directory Created", f"Directory '{new_folder}' created successfully.")
    else:
        messagebox.showinfo("Directory Exists", f"Directory '{new_folder}' already exists.")
    return new_folder


def needed_directories(user_path):
    # Create directory names for files
    directories_dict = {
        "SortedPictures": [".png", ".jpg", ".jpeg", ".gif",".PNG"],
        "SortedApplications": [".exe", ".apk", ".bat", ".com", ".wsf", ".bin"],
        "SortedArchives": [".zip", ".rar"],
        "SortedDocuments": [".pdf", ".docx", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".wpd"],
        "SortedVideo": [".mp4", ".mov", ".avi", ".vob", ".wmv", ".mpeg", ".mpg", ".flv", "3gp"],
        "SortedAudio": [".mp3", "wma", ".wpl", ".wav", ".mid", ".midi"],
        "SortedInternetFiles": [".html", ".htm", ".xhtml", ".rss", ".css", ".cer", ".asp", ".aspx", ".torrent"],
        "SortedSystemFiles": [".sys", ".tpm", ".icns", ".ini", ".cfg", ".msi", ".ico", ".dll"],
        "SortedCode": [".py", ".c", ".cpp", ".cs", ".java", ".PHP", ".swift", ".vb", ".js", ".jsl"]
    }

    # Initialize an empty set to store the needed directory names
    needed_dirs = set()

    # Scan through files in the user_path
    with os.scandir(user_path) as entries:
        for entry in entries:
            if entry.is_file():  # Ensure it's a file
                # Check each file extension against our directories
                for dir_name, extensions in directories_dict.items():
                    if any(entry.name.lower().endswith(ext) for ext in extensions):
                        needed_dirs.add(dir_name)
                        break

    # Create full paths for the needed directories
    needed_paths = {dir_name: os.path.join(user_path, dir_name) for dir_name in needed_dirs}

    return needed_paths


def organize_files(user_path, directories):
    # Associate the file extensions to their folder using Dict
    file_extensions_sorted = {
        ".png": "SortedPictures", ".jpg": "SortedPictures", ".jpeg": "SortedPictures", ".gif": "SortedPictures",".PNG": "SortedPictures",
        ".exe": "SortedApplications", ".apk": "SortedApplications", ".bat": "SortedApplications",
        ".com": "SortedApplications", ".wsf": "SortedApplications", ".bin": "SortedApplications",
        ".zip": "SortedArchives", ".rar": "SortedArchives",
        ".pdf": "SortedDocuments", ".docx": "SortedDocuments", ".doc": "SortedDocuments",
        ".xls": "SortedDocuments", ".xlsx": "SortedDocuments", ".ppt": "SortedDocuments",
        ".pptx": "SortedDocuments", ".txt": "SortedDocuments", ".rtf": "SortedDocuments", ".wpd": "SortedDocuments",
        ".mp4": "SortedVideo", ".mov": "SortedVideo", ".avi": "SortedVideo", ".vob": "SortedVideo",
        ".wmv": "SortedVideo", ".mpeg": "SortedVideo", ".mpg": "SortedVideo", ".flv": "SortedVideo",
        ".3gp": "SortedVideo",
        ".mp3": "SortedAudio", ".wma": "SortedAudio", ".wpl": "SortedAudio", ".wav": "SortedAudio",
        ".mid": "SortedAudio", ".midi": "SortedAudio",
        ".html": "SortedInternetFiles", ".htm": "SortedInternetFiles", ".xhtml": "SortedInternetFiles",
        ".rss": "SortedInternetFiles", ".css": "SortedInternetFiles", ".cer": "SortedInternetFiles",
        ".asp": "SortedInternetFiles", ".aspx": "SortedInternetFiles", ".torrent": "SortedInternetFiles",
        ".sys": "SortedSystemFiles", ".tpm": "SortedSystemFiles", ".icns": "SortedSystemFiles",
        ".ini": "SortedSystemFiles", ".cfg": "SortedSystemFiles", ".msi": "SortedSystemFiles",
        ".ico": "SortedSystemFiles", ".dll": "SortedSystemFiles",
        ".py": "SortedCode", ".c": "SortedCode", ".cpp": "SortedCode", ".cs": "SortedCode",
        ".java": "SortedCode", ".php": "SortedCode", ".swift": "SortedCode", ".vb": "SortedCode",
        ".js": "SortedCode", ".jsl": "SortedCode"
    }

    for dir_name in directories.values():
        create_directory(dir_name)

    with os.scandir(user_path) as entries:
        for entry in entries:
            if entry.is_file():
                for ext, dir_name in file_extensions_sorted.items():
                    if entry.name.endswith(ext) and dir_name in directories:
                        destination = directories[dir_name]
                        shutil.move(entry.path, destination)
                        print(f"Moved {entry.name} to {destination}")
                        break


def gui_start():
    user_path = select_directory()
    if user_path:
        directories = needed_directories(user_path)
        if directories:
            organize_files(user_path, directories)


if __name__ == "__main__":
    main()
