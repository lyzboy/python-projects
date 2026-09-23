import pathlib

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


def sort_files(root_path_string:str)->None:
    try:
        print("*** Starting Sort ***")
        # clean path string
        root_path_string = root_path_string.strip().strip('"').strip("'")
        # create a path to the root
        root_path = pathlib.Path(root_path_string)
        # for each resource in the root path
        for resource in root_path.iterdir():
                # if the resource is a file
                if resource.is_file():
                    # find the folder in the predefined list that matches the extension
                    matching_folder = [key for key, value_list in FOLDER_NAMES.items() if resource.suffix.lower() in value_list]
                    # if there is a matching folder in the list for this file's extension
                    if matching_folder:
                        # create the path for where to move this file
                        target_dir = root_path / matching_folder[0]
                        # create the directory at that path
                        target_dir.mkdir(parents=True, exist_ok=True)
                        # create the path that the file will be moved to
                        final_path = target_dir / resource.name
                        # move the file to that path, overwrites existing files of same name
                        resource.rename(final_path)
        print("*** Sorting Complete ***")
    except FileNotFoundError:
         print('The provided path is incorrect')

path = input("What is the folder to organize?\n")
sort_files(path)