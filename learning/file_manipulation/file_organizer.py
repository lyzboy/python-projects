import os
import pathlib

def list_files(path: str)->list | str:
    """Function that lists all files and folders within a provided path"""
    try:
        parsed_path = pathlib.PurePath(path)
        local_path = pathlib.Path(parsed_path)
        files = os.listdir(local_path);
        return files
    except FileNotFoundError:
        return f"Files not found or bad path"

path = input("What is the folder to organize?\n")
print(list_files(path))