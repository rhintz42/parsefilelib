def rec_fetch_children(file_obj, objs, file_lines, parent_indent, index):
    """
    Returns list of function objects

    Recursive wrapper
    """
    #TODO: REFACTOR THIS A LOT
    if index == len(file_lines):
        return index

    i = index
    while i < len(file_lines):
        l = file_lines[i]
        l_no_indent = l.lstrip()
        indent = len(l) - len(l_no_indent)

        if 'def' == l_no_indent[:3] or 'class' == l_no_indent[:5]:
            if indent <= parent_indent:
                return i-1

            if 'def' == l_no_indent[:3]:
                from parsefilelib.model.func_obj import FuncObj
                obj = FuncObj(file_obj, 'test')
                end_i = rec_fetch_children(file_obj, obj, file_lines, indent, i+1)
                obj.lines = file_lines[i:end_i+1]
                objs.append_child_function(obj)
            elif 'class' == l_no_indent[:5]:
                from parsefilelib.model.class_obj import ClassObj
                obj = ClassObj(file_obj, 'test')
                end_i = rec_fetch_children(file_obj, obj, file_lines, indent, i+1)
                obj.lines = file_lines[i:end_i+1]
                objs.append_child_class(obj)
            i = end_i
        i += 1

    return i

def get_folder_path_from_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])
