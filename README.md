# File Sorting Application
  #### Video Demo: https://www.youtube.com/watch?v=_eJnGlcdGzE

This Pyhton Script (with integrated GUI) helps you organize your files in a selected folder of choice by sorting them by category and creating folders for each.

## Features

- **GUI Interface**: Allows users to select a folder/directory via a user-friendly interface.
- **Sorting**: Automatically sorts the files into folders/directories based on their file extensions.

## How to Use
- The script has a GUI MODE, with an interactive display and ease of use.

## GUI Mode

### How to use
1. You run the script

2. Select the desired folder/directory of choice with the "Select Directory" button.

3. You just sit back while the script does its magic.

# Explaning "project.py" script

The script consists of multiple functions and multiple libraries for example Tkinter (for GUI), os (allows to interact with the Operating System), and shutil (provides a high-level file operation) 
### Let's start with the functions in the script:

1. **`main()`**: This is the main function of the program. It sets up the GUI by creating a window with a canvas to let the user access the folder/directory.

2. **`gui_start()`**: The "gui_start" function is triggered when the user clicks the "select directory" button

3. **`select_directory()`**: The function opens a file directory where the user selects his own folder from his computer. It returns the selected directory path.

4. **`needed_directories(user_path)`**: The function "needed_directories" checks all the files in the return of the "selected_directory" function, and determines all the necessary directories needed based on the files in the folder.

5. **`create_directory(new_folder)`**: The "create_directory" function creates a folder if it doesn't already exist. It displays a message showing whether the directory was created successfully and its location or if the folder already exists.

6. **`organize_files(user_path, directories)`**: The "organize_files" function organizes all the files in the user's path into their respective folder checking the extensions. This function iterates through every file checking the extensions and organizing them.

## Running the Script

To run this script you need to have a 3. x version of Python and have installed all the files from the "`Requirements.txt` file.

## Customization

You can change the script to your liking by modifying the `directories_dict` and `file_extensions_sorted` dicts to match all your files (in case I missed some). Simply add or remove the file extensions from each dict. (dict = dictionaries)

# Explaning "test_project.py" script

The `test_project.py` script contains tests for the functions created in the `project.py` script:

**`test_select_directory()`**

The "test_select_directory" function tests the `select_directory()` function. Using the patch function from unittest.mock it simulates the user selecting a directory from the computer. Then asserts that the returned directory matches the expected value.

**`test_create_directory()`**

The "test_create_directory" function tests the `create_directory()` function. Calls the function to create a directory and asserts that the directory exists.

**`test_needed_directories(tmpdir)`**

The "test_needed_directories" function tests the `needed_directories()` function. Creates a temporary folder using `tmpdir` from `pytest`. Then, create some test files with the given extension in the directory. After calling `needed_directories()`, it asserts that the returned dictionary of directories matches the expected result based on the file extensions.

**`test_organize_files()`**

The "test_organize_files" function tests the `organize_files()` function. This function creates a test directory with some test files and directories. Then, it calls the `organize_files()` function with the test directory and a dictionary of directories. In the end, asserts that the files are successfully and correctly moved into their respective folders.

## The Requirements.txt file

In this file are all the libraries that you need for running these scripts.

I used an app called grammarly for some words so take that with a pich of salt.(english is not my first language)
