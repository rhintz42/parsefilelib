def file_to_list(filepath):
    """
    Return all the lines of a file and return them as an array
    """
    try:
        with open(filepath) as f:
            file_lines = f.readlines()
    except IOError as e:
        # TODO: ERROR LOGGING
        return []
    
    return file_lines
