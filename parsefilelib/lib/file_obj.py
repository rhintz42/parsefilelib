def get_folder_path_from_file_path(file_path):
    """
    Return the folder path given a file's path
    """
    return '/'.join(file_path.split('/')[:-1])
