def get_folder_path_from_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])
