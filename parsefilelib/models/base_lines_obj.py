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
            self.file_lines = file_to_list(file_path)
            self.file_str = ''.join(self.file_lines)

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
        """
        Return the ast_node property
        """
        return self._ast_node

    @property
    def classes(self):
        """
        Return the classes property
        """
        return self._classes

    @property
    def children(self):
        """
        Return a list of the classes and functions properties combined
        """
        return self.classes + self.functions

    @property
    def comments(self):
        """
        Return the comments property if the Object has one, None otherwise
        """
        if hasattr(self, '_comments'):
            return self._comments
        return None

    @property
    def decorators(self):
        """
        Return the decorators property if the Object has one, None otherwise
        """
        if hasattr(self, '_decorators'):
            return self._decorators
        return None

    @property
    def docstring(self):
        """
        Return the docstring property if the Object has one, None otherwise
        """
        if hasattr(self, '_docstring'):
            return self._docstring
        return None

    @property
    def functions(self):
        """
        Return the functions property
        """
        return self._functions

    @property
    def imports(self):
        """
        Return the imports property if the Object has one, None otherwise
        """
        if hasattr(self, '_imports'):
            return self._imports
        return None

    @property
    def indent(self):
        """
        Return the indent property if the Object has one, None otherwise
        """
        if hasattr(self, '_indent'):
            return self._indent
        return None

    @property
    def is_class(self):
        """
        Return True if this Object is a 'class', false otherwise
        """
        return self._obj_type == 'class'

    @property
    def is_function(self):
        """
        Return True if this Object is a 'function', false otherwise
        """
        return self._obj_type == 'function'
    
    @property
    def line_number(self):
        """
        Return the line_number this Object starts on
        """
        return self.line_index_start + 1
    
    @property
    def line_index_def_class(self):
        """
        Return the line_index_def_class property
        """
        if hasattr(self, '_line_index_def_class'):
            return self._line_index_def_class
        return 0
    
    @property
    def line_index_end(self):
        """
        Return the line_index_end property
        """
        if hasattr(self, '_line_index_end'):
            return self._line_index_end
        return 0
    
    @property
    def line_index_start(self):
        """
        Return the line_index_start property
        """
        if hasattr(self, '_line_index_start'):
            return self._line_index_start
        return 0

    @property
    def code(self):
        """
        Return the lines property
        """
        return self.lines

    @property
    def lines(self):
        """
        Return the lines property
        """
        if hasattr(self, '_lines'):
            return self._lines
        return None

    @property
    def name(self):
        """
        Return the name property
        """
        if hasattr(self, '_name'):
            return self._name
        return None

    @property
    def num_lines(self):
        """
        Return the number of lines of this Object
        """
        if self.lines:
            return len(self.lines)
        return 0

    @property
    def obj_type(self):
        """
        Return the obj_type property if the Object has one, None otherwise
        """
        if hasattr(self, '_obj_type'):
            return self._obj_type
        return None

    @property
    def file_name(self):
        """
        Return the file_name property if the Object has one, None otherwise
        """
        if self.parent_file:
            return self.parent_file.name
        return None

    @property
    def file_path(self):
        """
        Return the file_path property if the Object has one, None otherwise
        """
        if self.parent_file:
            return self.parent_file.path
        return None

    @property
    def parent_file(self):
        """
        Return the parent_file property if the Object has one, None otherwise
        """
        if hasattr(self, '_parent_file'):
            return self._parent_file
        return None

    @property
    def parent_obj(self):
        """
        Return the parent_obj property if the Object has one, None otherwise
        """
        if hasattr(self, '_parent_obj'):
            return self._parent_obj
        return None

    @property
    def variables(self):
        """
        Return the variables property
        """
        if hasattr(self, '_variables'):
            return self._variables
        return None

    @property
    def returns(self):
        """
        Return the returns property
        """
        if hasattr(self, '_returns'):
            return self._returns
        return None


    """ SETTERS """

    @ast_node.setter
    def ast_node(self, value):
        """
        Set the ast_node property
        """
        self._ast_node = value

    @classes.setter
    def classes(self, value):
        """
        Set the classes property
        """
        self._classes = value

    @comments.setter
    def comments(self, value):
        """
        Set the comments property
        """
        self._comments = value

    @decorators.setter
    def decorators(self, value):
        """
        Set the decorators property
        """
        self._decorators = value

    @docstring.setter
    def docstring(self, value):
        """
        Set the docstring property
        """
        self._docstring = value

    @functions.setter
    def functions(self, value):
        """
        Set the functions property
        """
        self._functions = value
    
    @line_index_def_class.setter
    def line_index_def_class(self, value):
        """
        Set the line_index_def_class property
        """
        self._line_index_def_class = value
    
    @line_index_end.setter
    def line_index_end(self, value):
        """
        Set the line_index_end property
        """
        self._line_index_end = value
    
    @line_index_start.setter
    def line_index_start(self, value):
        """
        Set the line_index_start property
        """
        self._line_index_start = value

    @lines.setter
    def lines(self, value):
        """
        Set the lines property
        """
        self._lines = value

    @imports.setter
    def imports(self, value):
        """
        Set the imports property
        """
        self._imports = value

    @indent.setter
    def indent(self, value):
        """
        Set the indent property
        """
        self._indent = value

    @name.setter
    def name(self, value):
        """
        Set the name property
        """
        self._name = value

    @obj_type.setter
    def obj_type(self, value):
        """
        Set the obj_type property
        """
        self._obj_type = value

    @parent_file.setter
    def parent_file(self, value):
        """
        Set the parent_file property
        """
        self._parent_file = value

    @parent_obj.setter
    def parent_obj(self, value):
        """
        Set the parent_obj property
        """
        self._parent_obj = value

    @returns.setter
    def returns(self, value):
        """
        Set the returns property
        """
        self._returns = value

    @variables.setter
    def variables(self, value):
        """
        Set the variables property
        """
        self._variables = value


    """ FETCH METHODS """

    def fetch_child_functions(self):
        """
        Return the Functions that are within this Object
        """
        return self._fetch_children(fetch_obj_type='function')

    def fetch_child_classes(self):
        """
        Return the Classes that are within this Object
        """
        return self._fetch_children(fetch_obj_type='class')

    def fetch_child_decorators(self):
        """
        Return the Decorators that are within this Object
        """
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
        """
        Return the Imports that are within this Object
        """
        return self._fetch_children(fetch_obj_type='import')

    def fetch_child_returns(self):
        """
        Return the Returns that are within this Object
        """
        return self._fetch_children(fetch_obj_type='return')

    def fetch_child_variables(self):
        """
        Return the Variables that are within this Object
        """
        return self._fetch_children(fetch_obj_type='assign')


    """ APPEND """
    def append_child(self, obj):
        """
        Append a BaseLinesObj to this class. The BaseLinesObj needs to be
            either a function or a class
        """
        if obj.obj_type == 'function':
            self.append_function(obj)
        elif obj.obj_type == 'class':
            self.append_class(obj)

    def append_class(self, class_obj):
        """
        Append a BaseLinesObj to the classes property of this object that has
            obj_type of type 'class'
        """
        self._classes.append(class_obj)

    def append_comment(self, comment):
        """
        Append a Comment to the comments property of this Object
        """
        self._comments.append(comment)

    def append_decorator(self, decorator):
        """
        Append a Decorator to the decorators property of this Object
        """
        self._decorators.append(decorator)

    def append_function(self, func_obj):
        """
        Append a BaseLinesObj to the functoins property of this Object that has
            obj_type of type 'function'
        """
        self._functions.append(func_obj)

    def append_import(self, imp):
        """
        Append an Import to the imports property of this Object
        """
        self._imports.append(imp)

    def append_return(self, ret):
        """
        Append a Return to the returns property of this Object
        """
        self._returns.append(ret)

    def append_variable(self, v):
        """
        Append a Variable to the variables property of this Object
        """
        self._variables.append(v)


    """ GET METHODS """

    def to_dict(self):
        """
        Returns a dictionary representation of this object

        Stuff to note:
        * Don't print parent because we don't want to have a circular stuff
            going on
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
        """
        Return a list of children of this Object
        """
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
