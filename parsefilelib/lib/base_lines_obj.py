import ast

def fetch_ast_node(file_lines=None, name=None, max_index=None):
    """
    Return the ast node and end_line_index that matches the name object, or
        just the root if no name was given
    """
    if not file_lines:
        return None, max_index

    root = ast.parse(file_lines)

    if not name:
        return root, max_index

    return rec_fetch_ast_node(root, name, max_index)

def get_line_index_def_class(file_lines, start_index, max_index):
    """
    Return the end_line_index of the definition of the class or function object

    TODO: Check for indentation as well as do other checks to be sure it is the
    function definition (See `NOTE` section of this docstring)

    NOTE: This function needs a lot more tests to be done to it. The current
        implementation is not great because it doesn't account for if a
        decorator is spread out on multiple lines and starts with "def" or
        "class". It also doesn't account for comments above the function
        definition.
    """
    i = start_index
    while i < max_index:
        l = file_lines[i]
        l_no_indent = l.lstrip()

        if 'def' == l_no_indent[:3] or 'class' == l_no_indent[:5]:
            return i

        i += 1

    return max_index

def node_type(ast_node):
    """
    Return the type of ast node
    """
    if ast_node.__class__.__name__ == 'FunctionDef':
        return 'function'
    elif ast_node.__class__.__name__ == 'ClassDef':
        return 'class'
    elif ast_node.__class__.__name__ == 'Module':
        return 'file'
    elif ast_node.__class__.__name__ == 'Return':
        return 'return'
    elif ast_node.__class__.__name__ == 'Assign':
        return 'assign'
    elif ast_node.__class__.__name__ == 'Import':
        return 'import'
    elif ast_node.__class__.__name__ == 'ImportFrom':
        return 'import'
    elif ast_node.__class__.__name__ == 'Expr':
        return 'other'
    else:
        return 'other'

def rec_fetch_ast_node(root, name, max_index):
    """
    Return the end_index and ast node that has the name given
    """
    if not hasattr(root, 'body'):
        return None, max_index

    children = root.body

    #for child in children:
    i = 0
    while i < len(children):
        child = children[i]
        if not hasattr(child, 'name'):
            i += 1
            continue
        if child.name == name:
            if i+1 < len(children):
                line_index_end = children[i+1].lineno-2
            else:
                line_index_end = max_index
            return child, line_index_end
        i += 1

    #for child in children:
    i = 0
    while i < len(children):
        child = children[i]
        if i+1 < len(children):
            m_index = children[i+1].lineno-2
        else:
            m_index = max_index

        node, line_index_end = rec_fetch_ast_node(child, name, m_index)
        if node:
            return node, line_index_end
        i += 1

    return None, max_index
    
