def get_child_functions(file_lines):
    """
    Returns list of function objects
    """
    function_definitions = []

    for l in file_lines:
        if 'def' in l:
            function_definitions.append(l)

    return function_definitions
