from os import listdir
from os.path import isdir, isfile

def get_child_file_names(folder_path):
    file_names_in_folder = []
    try:
        for f in listdir(folder_path):
            if '.pyc' not in f and '.swp' not in f and isfile("%s/%s" %(folder_path,f)):
                file_names_in_folder.append(f)
    except OSError as e:
        # error
        print("ERROR IN get_child_file_names")

    return file_names_in_folder

def get_child_folder_names(folder_path):
    folder_names_in_folder = []
    try:
        for f in listdir(folder_path):
            if '__pycache__' not in f and isdir("%s/%s" %(folder_path,f)):
                folder_names_in_folder.append(f)
    except OSError as e:
        # error
        print("ERROR IN get_child_folder_names")

    return folder_names_in_folder

def format_folder_path(folder_path):
    if folder_path[-1] != '/':
        folder_path += '/'

    return folder_path
