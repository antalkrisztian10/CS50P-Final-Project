""" I only tested the "real" functions beacuse the GUI test require different tools."""

import os
import shutil
from unittest.mock import patch
from project import create_directory, needed_directories, organize_files, select_directory


def test_select_directory():
    # Mock the filedialog.askdirectory function to return a predefined directory
    with patch('project.filedialog.askdirectory', return_value='/path/to/directory'):
        directory = select_directory()
        assert directory == '/path/to/directory'


def test_create_directory():
    new_folder = "test_folder"
    create_directory(new_folder)
    assert os.path.exists(new_folder)


def test_needed_directories(tmpdir):
    user_path = tmpdir.mkdir("test_directory")
    directories = needed_directories(str(user_path))
    assert isinstance(directories, dict)

    open(os.path.join(str(user_path), "test_file1.png"), "w").close()
    open(os.path.join(str(user_path), "test_file2.exe"), "w").close()
    open(os.path.join(str(user_path), "test_file3.pdf"), "w").close()
    open(os.path.join(str(user_path), "test_file4.zip"), "w").close()

    expected_result = {
        "SortedPictures": os.path.join(str(user_path), "SortedPictures"),
        "SortedApplications": os.path.join(str(user_path), "SortedApplications"),
        "SortedDocuments": os.path.join(str(user_path), "SortedDocuments"),
        "SortedArchives": os.path.join(str(user_path), "SortedArchives")
    }

    result = needed_directories(str(user_path))

    assert result == expected_result


def test_organize_files():
    user_path = "test_directory"

    # Delete the directory if it already exists
    if os.path.exists(user_path):
        shutil.rmtree(user_path)

    os.mkdir(user_path)
    open(os.path.join(user_path, "test_file1.png"), "w").close()
    open(os.path.join(user_path, "test_file2.exe"), "w").close()
    open(os.path.join(user_path, "test_file3.pdf"), "w").close()
    open(os.path.join(user_path, "test_file4.zip"), "w").close()

    directories = {
        "SortedPictures": os.path.join(user_path, "SortedPictures"),
        "SortedApplications": os.path.join(user_path, "SortedApplications"),
        "SortedDocuments": os.path.join(user_path, "SortedDocuments"),
        "SortedArchives": os.path.join(user_path, "SortedArchives")
    }

    organize_files(user_path, directories)

    assert os.path.exists(os.path.join(directories["SortedPictures"], "test_file1.png"))
    assert os.path.exists(os.path.join(directories["SortedApplications"], "test_file2.exe"))
    assert os.path.exists(os.path.join(directories["SortedDocuments"], "test_file3.pdf"))
    assert os.path.exists(os.path.join(directories["SortedArchives"], "test_file4.zip"))
