def _get_string_end_index(func_code_lines, docstring_start_index):
    """ Get End of Docstring line # """
    if func_code_lines[docstring_start_index].count('"""') == 2 or \
        func_code_lines[docstring_start_index].count("'''") == 2:
        return docstring_start_index
        
    for i,l in enumerate(func_code_lines[docstring_start_index+1:],
                         start=docstring_start_index+1):
        if '"""' in l or "'''" in l:
            return i

    return len(func_code_lines) - 1

def get_function_name(line):
    l_no_indent = line.lstrip()
    return line.split('(')[0][4:]

def get_class_name(line):
    l_no_indent = line.lstrip()
    return line.split('(')[0][6:]

def fetch_comment(file_lines, index):
    comment_start_i = index

    if comment_start_i >= len(file_lines):
        return comment_start_i, None

    l = file_lines[comment_start_i]
    l_no_indent = l.lstrip()

    #import pdb;pdb.set_trace()
    if '"""' in l_no_indent or "'''" in l_no_indent:
        # Get the comment and attach to the parent object
        comment_end_i = _get_string_end_index(file_lines, comment_start_i)
        comment = file_lines[comment_start_i:comment_end_i+1]
        return comment_end_i + 1, comment
    
    return index, None

def fetch_docstring(parent_obj, file_lines, func_def_index):
    docstring_start_i = func_def_index + 1

    if docstring_start_i >= len(file_lines):
        return docstring_start_i

    l = file_lines[docstring_start_i]
    l_no_indent = l.lstrip()

    if '"""' == l_no_indent[:3] or "'''" == l_no_indent[:3]:
        # Get the docstring and attach to the parent object
        docstring_end_i = _get_string_end_index(file_lines, docstring_start_i)
        docstring = file_lines[docstring_start_i:docstring_end_i+1]
        parent_obj.append_child_docstring(docstring)
        return docstring_end_i + 1
    
    return func_def_index

#def fetch_child_objects():
def create_child_obj(file_obj, parent_obj, file_lines, parent_indent, index):
    from parsefilelib.model.func_obj import BaseLineObj

    l = file_lines[index]
    l_no_indent = l.lstrip()
    indent = len(l) - len(l_no_indent)

    if 'def' == l_no_indent[:3]:
        obj = BaseLineObj('function', file_obj, get_function_name(l_no_indent))
    elif 'class' == l_no_indent[:5]:
        obj = BaseLineObj('class', file_obj, get_class_name(l_no_indent))

    # TODO: Get all Decorators
    index = fetch_docstring(obj, file_lines, index)

    end_i = rec_fetch_children(file_obj, obj, file_lines, indent, index+1)
    obj.lines = file_lines[index:end_i+1]
    parent_obj.append_child(obj)

    return end_i

def rec_fetch_children(file_obj, parent_obj, file_lines, parent_indent, index):
    """
    Returns list of function objects

    Recursive wrapper
    """
    if index >= len(file_lines):
        return index

    i = index
    while i < len(file_lines):
        l = file_lines[i]
        
        # TODO: Check for Variable, `continue` if found
        # TODO: Check for Return, `continue` if found

        # TODO: Check line for Multi-Line String, `continue` if found
        if '"""' in l or "'''" in l:
            end_i, comment = fetch_comment(file_lines, i)
            i = end_i

        # TODO: Check Line for Import, `continue` if found

        l_no_indent = l.lstrip()
        indent = len(l) - len(l_no_indent)
        
        if 'def' == l_no_indent[:3] or 'class' == l_no_indent[:5]:
            if indent <= parent_indent:
                return i-1

            end_i = create_child_obj(file_obj, parent_obj, file_lines, parent_indent, i)
            i = end_i

        i += 1

    return i

def get_folder_path_from_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])
