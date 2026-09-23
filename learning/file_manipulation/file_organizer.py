from pathlib import Path
import json

LIBRARY_NAME = "file_organizer_folders.json"
DEFAULT_CONFIG = {
            "Models": [".step", ".sldprt", ".stp", ".stl"],
            "Images": [".png", ".jpeg", ".jpg"],
            "Zipped": [".zip"],
            "Installs": [".exe", ".msi", ".iso"],
            "Excels": [".csv"],
            "Web": [".html", ".css", ".js", ".md", ".json"],
            "PDF": [".pdf"],
            "Documents": [".doc", ".txt", ".docx"],
            "Logs": [".log"]
            }
ROOT_PATH = Path(__file__).resolve().parent
CONFIG_PATH = ROOT_PATH / LIBRARY_NAME

def load_config()-> dict:
    # the root path of the current py file
    root_path = ROOT_PATH
    # create a path using the dictionary file name constant
    dictionary_file_path = CONFIG_PATH
    if dictionary_file_path.exists():
        print("There is a dictionary file.")
        # read the text from the file using path
        json_file = dictionary_file_path.read_text()
        # parse the json data read from the file
        folder_names = json.loads(json_file)
        return folder_names
    else:
        print("There is no dictionary file. A file name 'file_organizer_folders.json' should be saved in the same folder as this script. If it is deleted or moved, a generic list will be used.")
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

def save_config(config:dict)-> None:
    config_path = CONFIG_PATH
    print("Encoding the library...")
    parsed_json = json.dumps(config, indent=4)
    print("Writing the library to file...")
    config_path.write_text(parsed_json)
    print("Library save complete!")


def sort_files(root_path_string:str, folder_names: dict = None)->None:
    try:
        if folder_names is None:
             folder_names = DEFAULT_CONFIG
        print("*** Starting Sort ***")
        # clean path string
        root_path_string = root_path_string.strip().strip('"').strip("'")
        # create a path to the root
        root_path = Path(root_path_string)
        # for each resource in the root path
        for resource in root_path.iterdir():
                # if the resource is a file
                if resource.is_file():
                    # find the folder in the predefined list that matches the extension
                    matching_folder = [key for key, value_list in folder_names.items() if resource.suffix.lower() in value_list]
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

if __name__ == "__main__":
    path = input("What is the folder to organize?\n")
    sort_files(path)