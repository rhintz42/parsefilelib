import ast
from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.models.base_obj import BaseObj
from parsefilelib.lib.base_lines_obj import fetch_ast_node,\
                                            get_line_index_def_class,\
                                            node_type,\
                                            rec_fetch_ast_node


class BaseLinesObj(object):
    """
    An object that encapsulates all details of a Lines object
    """

    def __init__(self, def_name=None, ast_node=None, parent_obj=None,
                    parent_file=None, file_lines=None, line_number=0, indent=0,
                    file_path=None, line_index_end=0, get_children=True):
        """
        init method for the BaseLinesObj
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
            try:
                self.ast_node, self.line_index_end = fetch_ast_node(file_lines=self.file_str,
                                                                    name=def_name,
                                                                    max_index=self.line_index_end)
            #TODO: There are errors when you try to compile non-python objects.
            #       Need to catch them and do something proper with them
            except SyntaxError as e:
                self.ast_node = None
            except TypeError as e:
                self.ast_node = None

        if not self.ast_node:
            return

        self.obj_type = node_type(self.ast_node)

        # Put this conditional stuff into the file object
        if node_type(self.ast_node) == 'file':
            #self.name = self.file_name
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
    def children(self):
        return self.classes + self.functions

    @property
    def comments(self):
        if hasattr(self, '_comments'):
            return self._comments
        return None

    @property
    def decorators(self):
        if hasattr(self, '_decorators'):
            return self._decorators
        return None

    @property
    def docstring(self):
        if hasattr(self, '_docstring'):
            return self._docstring
        return None

    @property
    def functions(self):
        return self._functions

    @property
    def imports(self):
        if hasattr(self, '_imports'):
            return self._imports
        return None

    @property
    def indent(self):
        if hasattr(self, '_indent'):
            return self._indent
        return None

    @property
    def is_class(self):
        return self._obj_type == 'class'

    @property
    def is_function(self):
        return self._obj_type == 'function'
    
    @property
    def line_number(self):
        return self.line_index_start + 1
    
    @property
    def line_index_def_class(self):
        return self._line_index_def_class
    
    @property
    def line_index_end(self):
        return self._line_index_end
    
    @property
    def line_index_start(self):
        return self._line_index_start

    @property
    def code(self):
        return self.lines

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
        if hasattr(self, '_obj_type'):
            return self._obj_type
        return None

    @property
    def file_name(self):
        if self.parent_file:
            return self.parent_file.name
        return None

    @property
    def file_path(self):
        if self.parent_file:
            return self.parent_file.path
        return None

    @property
    def parent_file(self):
        if hasattr(self, '_parent_file'):
            return self._parent_file
        return None

    @property
    def parent_obj(self):
        if hasattr(self, '_parent_obj'):
            return self._parent_obj
        return None

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
    
    @line_index_def_class.setter
    def line_index_def_class(self, value):
        self._line_index_def_class = value
    
    @line_index_end.setter
    def line_index_end(self, value):
        self._line_index_end = value
    
    @line_index_start.setter
    def line_index_start(self, value):
        self._line_index_start = value

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


    """ FETCH METHODS """

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


    """ APPEND """
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
        if not self.obj_type:
            return {}

        return {
            'classes': [c.to_dict() for c in self.classes],
            'comments': self.comments,
            'decorators': self.decorators,
            'docstring': self.docstring,
            'functions': [f.to_dict() for f in self.functions],
            'children': [c.to_dict() for c in self.children],
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


    """ Private Methods """

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
