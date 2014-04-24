from os import listdir
from os.path import isdir, isfile, join

def get_child_file_names(folder_path):
    files_in_folder = []
    try:
        for f in listdir(folder_path):
            if '.pyc' not in f and isfile("%s/%s" %(folder_path,f)):
                files_in_folder.append(f)
    except OSError as e:
        # error
        print("ERROR IN get_child_file_names")

    return files_in_folder

def get_child_folder_names(folder_path):
    folders_in_folder = [ f for f in listdir(folder_path) if isdir("%s/%s" %(folder_path,f)) ]

    return folders_in_folder
