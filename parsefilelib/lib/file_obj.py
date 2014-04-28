import re

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

def fetch_variable(file_lines, index):
    end_i = index
    variable_definition = file_lines[index]

    return end_i, variable_definition


def get_folder_path_from_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])
