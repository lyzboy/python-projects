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
    "Documents":[".doc",".txt",".docx"],
    "Logs":[".log"]
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
    print("Sorting files...")
    for file in found_files:
            file_extension = os.path.splitext(file)[-1].lower()
            matching_folder = [key for key, value_list in FOLDER_NAMES.items()
             if file_extension in value_list]

            # this checks if there is a folder for the extension based on the dictionary above and skips creation of so
            if not matching_folder:
                continue

            # check here if a folder exists for the file and if not create it.
            if not matching_folder[0] in found_dirs:
                print(f'There is not a {matching_folder[0]} folder')
                print(f'Creating {matching_folder[0]} folder...')
                p = pathlib.Path(root/matching_folder[0])
                p.mkdir()
                found_dirs.append(matching_folder[0])
                print('Folder created')
            destination = pathlib.Path(root/matching_folder[0]/file)
            original_path = pathlib.Path(root/file)
            print(f'Moving {original_path} to {destination}')
            os.replace(original_path, destination)
    print("*** Sorting Complete ***")
        
    

path = input("What is the folder to organize?\n")
place_files(path)
