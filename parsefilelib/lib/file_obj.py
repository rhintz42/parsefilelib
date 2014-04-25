import re

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

    if '"""' in l_no_indent or "'''" in l_no_indent:
        # Get the comment and attach to the parent object
        comment_end_i = _get_string_end_index(file_lines, comment_start_i)
        comment = file_lines[comment_start_i:comment_end_i+1]
        return comment_end_i, comment
    
    return index, None

def is_docstring(lines):
    return '"""' == lines[0].lstrip()[:3] or "'''" == lines[0].lstrip()[:3]

def fetch_docstring(parent_obj, file_lines, func_def_index):
    doc_start_index = func_def_index + 1

    end_i, comment = fetch_comment(file_lines, doc_start_index)
    if comment and is_docstring(comment):
        parent_obj.append_docstring(comment)
        return end_i
    return func_def_index

def is_decorator(line):
    return '@' == line.lstrip()[:1]

def fetch_decorators(parent_obj, file_lines, func_def_index):
    index = func_def_index - 1

    i = index
    while i > 0 and is_decorator(file_lines[i]):
        parent_obj.append_decorator(file_lines[i])
        i -= 1

def create_child_obj(file_obj, parent_obj, file_lines, parent_indent, index):
    from parsefilelib.model.base_lines_obj import BaseLinesObj

    l = file_lines[index]
    l_no_indent = l.lstrip()
    indent = len(l) - len(l_no_indent)

    if 'def' == l_no_indent[:3]:
        obj = BaseLinesObj('function', file_obj, get_function_name(l_no_indent),
                           indent=indent)
    elif 'class' == l_no_indent[:5]:
        obj = BaseLinesObj('class', file_obj, get_class_name(l_no_indent),
                           indent=indent)

    fetch_decorators(obj, file_lines, index)

    # TODO: Get all Decorators
    index = fetch_docstring(obj, file_lines, index)

    end_i = rec_fetch_children(file_obj, obj, file_lines, indent, index+1)
    obj.lines = file_lines[index:end_i+1]
    parent_obj.append_child(obj)

    return end_i

def fetch_variable(file_lines, index):
    end_i = index
    variable_definition = file_lines[index]

    return end_i, variable_definition

def rec_fetch_children(file_obj, parent_obj, file_lines, parent_indent, index):
    """
    Returns list of function objects

    Recursive wrapper
    """
    #import ast

    #a = ast.parse(open(file_obj.path, 'r').read())
    #w = ast.walk(a)
    #for n in w:
    #    import pdb;pdb.set_trace()

    if index >= len(file_lines):
        return index

    i = index
    while i < len(file_lines):
        l = file_lines[i]
        l_no_indent = l.lstrip()
        indent = len(l) - len(l_no_indent)

        if indent <= parent_indent:
            return i-1
        
        # TODO: Check for Variable, append if found
        single_equal = re.compile('.*[^=]=[^=].*')
        if single_equal.search(l):
            end_i, v = fetch_variable(file_lines, i)
            parent_obj.append_variable(v)
            i = end_i

        # TODO: Check for Return
        if 'return' == l_no_indent[:6]:
            end_i, v = fetch_variable(file_lines, i)
            parent_obj.append_return(v)
            i = end_i

        # TODO: This currently just appends no matter what, but should only do if an actual comment
        # TODO: Add 'is_comment' boolean
        if '"""' in l or "'''" in l:
            end_i, comment = fetch_comment(file_lines, i)
            parent_obj.append_comment(comment)
            i = end_i + 1
            continue

        # TODO: Check Line for Import, `continue` if found
        
        if 'def' == l_no_indent[:3] or 'class' == l_no_indent[:5]:
            end_i = create_child_obj(file_obj, parent_obj, file_lines, parent_indent, i)
            i = end_i + 1
            continue

        i += 1

    return i

def get_folder_path_from_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])
