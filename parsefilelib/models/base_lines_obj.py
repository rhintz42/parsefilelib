import ast
from parsefilelib.lib.file_obj import fetch_comment
from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.models.base_obj import BaseObj


def rec_fetch_ast_node(root, name, max_index):
    if not hasattr(root, 'body'):
        return None, max_index

    children = root.body

    #for child in children:
    i = 0
    while i < len(children):
        child = children[i]
        if not hasattr(child, 'name'):
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
    

def fetch_ast_node(file_lines=None, name=None, max_index=None):
    if not file_lines:
        return None, max_index

    root = ast.parse(file_lines)

    if not name:
        return root, max_index

    return rec_fetch_ast_node(root, name, max_index)

def node_type(ast_node):
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

def get_line_index_def_class(file_lines, start_index, max_index):
    i = start_index
    while i < max_index:
        l = file_lines[i]
        l_no_indent = l.lstrip()

        if 'def' == l_no_indent[:3] or 'class' == l_no_indent[:5]:
            return i

        i += 1

    return max_index

class BaseLinesObj(object):
    """
    An object the encapsulates all details of a Lines object
    """
    def fetch_child_functions(self):
        return self._fetch_children(fetch_obj_type='function')

    def fetch_child_classes(self):
        return self._fetch_children(fetch_obj_type='class')

    def fetch_child_decorators(self):
        i = 0
        children = self.ast_node.decorator_list
        decorators = []
        while i < len(children):
            if i+1 < len(children):
                line_index_end = children[i+1].lineno-2
            else:
                line_index_end = self.line_index_def_class

            d = children[i]
            decorators.append(BaseObj(
                    d,
                    obj_type='decorator',
                    line_index_end=line_index_end,
                    parent_obj=self)
                )
            i += 1
        return decorators

    def fetch_child_imports(self):
        return self._fetch_children(fetch_obj_type='import')

    def fetch_child_returns(self):
        return self._fetch_children(fetch_obj_type='return')

    def fetch_child_variables(self):
        return self._fetch_children(fetch_obj_type='assign')

    def _fetch_children(self, fetch_obj_type='function'):
        root = self.ast_node

        if not hasattr(root, 'body'):
            return []

        obj_list = []
        children = root.body

        i = 0
        while i < len(children):
            child = children[i]
            if node_type(child) == fetch_obj_type:
                if i+1 < len(children):
                    line_index_end = children[i+1].lineno-2
                else:
                    line_index_end = self.line_index_end

                if fetch_obj_type == 'function' or fetch_obj_type == 'class' or fetch_obj_type == 'file':
                    obj_list.append(BaseLinesObj(
                        ast_node=child,
                        file_lines=self.file_lines,
                        line_index_end=line_index_end,
                        def_name=child.name,
                        parent_obj=self,
                        parent_file=self.parent_file)
                    )
                else:
                    obj_list.append(BaseObj(
                        child,
                        line_index_end=line_index_end,
                        parent_obj=self,
                        parent_file=self.parent_file)
                    )
            i += 1

        return obj_list

    # TODO: FUNCTION LINES MAYBE DANGEROUS
    #   Look into further to see best way to handle
    #   Do recursion in these files
    #       Check to make sure function_name is in there, though
    def __init__(self, def_name=None, ast_node=None, parent_obj=None,
                    parent_file=None, file_lines=None, line_number=0, indent=0,
                    file_path=None, line_index_end=0, get_children=True):
        """
        init method for the BaseLinesObj

        the optional stuff:
        * file_path: used if there is no parent_file
        """
        if file_lines:
            self.file_lines = file_lines
            self.file_str = ''.join(self.file_lines)
        else:
            self.file_str = open(file_path, 'r').read()
            self.file_lines = file_to_list(file_path)

        if line_index_end == 0:
            self.line_index_end = len(self.file_lines)-1
        else:
            self.line_index_end = line_index_end

        # Set ast_node
        if ast_node:
            self.ast_node = ast_node
        else:
            self.ast_node, self.line_index_end = fetch_ast_node(file_lines=self.file_str,
                                                                name=def_name,
                                                                max_index=self.line_index_end)

        if not self.ast_node:
            return

        self.obj_type = node_type(self.ast_node)

        if node_type(self.ast_node) == 'file':
            self.name = self.file_name
            self.indent = -1
            self.line_index_start = 0
            self.line_index_def_class = 0
            self.decorators = []
            self.parent_file = self
            self.parent_obj = parent_obj
        else:
            self.name = self.ast_node.name
            self.indent = self.ast_node.col_offset
            self.line_index_start = self.ast_node.lineno - 1
            self.line_index_def_class = get_line_index_def_class(self.file_lines,
                                                        self.line_index_start,
                                                        self.line_index_end)
            self.decorators = []

            self.decorators = self.fetch_child_decorators()
            if parent_obj:
                self.parent_file = parent_file
                self.parent_obj = parent_obj
            else:
                from parsefilelib.models.file_obj import FileObj
                self.parent_obj = FileObj(file_path, child=self)
                self.parent_file = self.parent_obj

        self.comments = []

        self.lines = self.file_lines[self.line_index_start:self.line_index_end+1]
        self.line_str = ''.join(self.lines)

        if get_children:
            self.classes = self.fetch_child_classes()
            self.functions = self.fetch_child_functions()

        self.docstring = ast.get_docstring(self.ast_node)
        self.imports = self.fetch_child_imports()
        self.returns = self.fetch_child_returns()
        self.variables = self.fetch_child_variables()

    """ GETTERS """
    @property
    def ast_node(self):
        return self._ast_node

    @property
    def classes(self):
        return self._classes

    @property
    def comments(self):
        return self._comments

    @property
    def decorators(self):
        return self._decorators

    @property
    def docstring(self):
        return self._docstring

    @property
    def functions(self):
        return self._functions

    @property
    def imports(self):
        return self._imports

    @property
    def indent(self):
        return self._indent

    @property
    def is_class(self):
        return self._obj_type == 'class'

    @property
    def is_function(self):
        return self._obj_type == 'function'

    @property
    def lines(self):
        return self._lines

    @property
    def name(self):
        return self._name

    @property
    def num_lines(self):
        return len(self.lines)

    @property
    def obj_type(self):
        return self._obj_type

    @property
    def parent_file(self):
        return self._parent_file

    @property
    def parent_obj(self):
        return self._parent_obj

    @property
    def variables(self):
        return self._variables

    @property
    def returns(self):
        return self._returns

    """ SETTERS """
    @ast_node.setter
    def ast_node(self, value):
        self._ast_node = value

    @classes.setter
    def classes(self, value):
        self._classes = value

    @comments.setter
    def comments(self, value):
        self._comments = value

    @decorators.setter
    def decorators(self, value):
        self._decorators = value

    @docstring.setter
    def docstring(self, value):
        self._docstring = value

    @functions.setter
    def functions(self, value):
        self._functions = value

    @lines.setter
    def lines(self, value):
        self._lines = value

    @imports.setter
    def imports(self, value):
        self._imports = value

    @indent.setter
    def indent(self, value):
        self._indent = value

    @name.setter
    def name(self, value):
        self._name = value

    @obj_type.setter
    def obj_type(self, value):
        self._obj_type = value

    @parent_file.setter
    def parent_file(self, value):
        self._parent_file = value

    @parent_obj.setter
    def parent_obj(self, value):
        self._parent_obj = value

    @returns.setter
    def returns(self, value):
        self._returns = value

    @variables.setter
    def variables(self, value):
        self._variables = value

    """ APPEND FUNCTIONS """
    def append_child(self, obj):
        if obj.obj_type == 'function':
            self.append_function(obj)
        elif obj.obj_type == 'class':
            self.append_class(obj)

    def append_class(self, class_obj):
        self._classes.append(class_obj)

    def append_comment(self, comment):
        self._comments.append(comment)

    def append_decorator(self, decorator):
        self._decorators.append(decorator)

    def append_function(self, func_obj):
        self._functions.append(func_obj)

    def append_import(self, imp):
        self._imports.append(imp)

    def append_return(self, ret):
        self._returns.append(ret)

    def append_variable(self, v):
        self._variables.append(v)

    """ GET METHODS """

    def to_dict(self):
        """
        Returns ...

        Stuff to note:
        * Don't print parent because we don't want to have a circular thing
            going
        * Don't need num_lines, kind of pointless for others because they have
            access to lines and the python library
        """
        return {
            'classes': [c.to_dict() for c in self.classes],
            'comments': self.comments,
            'decorators': self.decorators,
            'docstring': self.docstring,
            'functions': [f.to_dict() for f in self.functions],
            'imports': self.imports,
            'indent': self.indent,
            'is_class': self.is_class,
            'is_function': self.is_function,
            'lines': self.lines,
            'line_index_start': self.line_index_start,
            'line_index_end': self.line_index_end,
            'name': self.name,
            'obj_type': self.obj_type,
            'parent_file_path': self.parent_file.path,
            'variables': self.variables,
            'returns': self.returns
        }
