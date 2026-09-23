import os
import pathlib

found_dirs = []
found_files = []
FOLDER_NAMES = {
    "Models":[".step",".sldprt",".stp",".stl"], 
    "Images":[".png",".jpeg",".jpg"],
    "Zipped":[".zip"],
    "Installs":[".exe",".msi",".iso"],
    "Excels":[".csv"],
    "Web":[".html",".css",".js",".md",".json"],
    "PDF":[".pdf"],
    "Documents":[".doc",".txt",".docx"]
    }

def list_files(path: str)-> str | None:
    """Add all files to constant lists"""
    try:
        print('Searching directory...')
        parsed_path = pathlib.PurePath(path)
        local_path = pathlib.Path(parsed_path)
        resources = os.scandir(local_path);
        for resource in resources:
            if resource.is_file():
                found_files.append(resource.name)
            else:
                found_dirs.append(resource.name)
        return None
    except FileNotFoundError:
        return f"Files not found or bad path"


# TODO: only create folders that will be needed for files.
def place_files(path)->None:
    """Moves files to organized folder locations"""
    path = path.replace('"', '')
    list_files(path)
    root = pathlib.Path(path)
    print("Checking organized folder structure...")
    for name in FOLDER_NAMES.keys():
        if not name in found_dirs:
            print(f'There is not a {name} folder')
            print(f'Creating {name} folder...')
            p = pathlib.Path(root/name)
            p.mkdir()
            print('Folder created')
    print("Sorting files...")
    for file in found_files:
            file_extension = os.path.splitext(file)[-1].lower()
            matching_folder = [key for key, value_list in FOLDER_NAMES.items() if file_extension in value_list]
            if not matching_folder:
                continue
            destination = pathlib.Path(root/matching_folder[0]/file)
            original_path = pathlib.Path(root/file)
            print(f'Moving {original_path} to {destination}...')
            os.replace(original_path, destination)
    print("*** Sorting Complete ***")
        
    

path = input("What is the folder to organize?\n")
place_files(path)
