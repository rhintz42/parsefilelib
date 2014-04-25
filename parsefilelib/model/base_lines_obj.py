class BaseLinesObj(object):
    """
    An object the encapsulates all details of a Lines object
    """

    # TODO: FUNCTION LINES MAYBE DANGEROUS
    #   Look into further to see best way to handle
    #   Do recursion in these files
    #       Check to make sure function_name is in there, though
    def __init__(self, obj_type, file_obj, name, lines=None, indent=0):
        """
        init method for the BaseLinesObj
        """
        self.parent_file = file_obj
        self.name = name
        self.obj_type = obj_type
        self.indent = indent

        self.classes = []
        self.comments = []
        self.decorators = []
        self.docstrings = []
        self.functions = []
        self.imports = []
        self.returns = []
        self.variables = []

        if lines:
            self.lines = lines

    """ GETTERS """
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
    def docstrings(self):
        return self._docstrings

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
    def variables(self):
        return self._variables

    @property
    def returns(self):
        return self._returns

    """ SETTERS """
    @classes.setter
    def classes(self, value):
        self._classes = value

    @comments.setter
    def comments(self, value):
        self._comments = value

    @decorators.setter
    def decorators(self, value):
        self._decorators = value

    @docstrings.setter
    def docstrings(self, value):
        self._docstrings = value

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
        else:
            self._docstrings.append(docstring)

    def append_class(self, class_obj):
        self._classes.append(class_obj)

    def append_comment(self, comment):
        self._comments.append(comment)

    def append_decorator(self, decorator):
        self._decorators.append(decorator)

    def append_docstring(self, docstring):
        self._docstrings.append(docstring)

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
            'docstrings': self.docstrings,
            'functions': [f.to_dict() for f in self.functions],
            'imports': self.imports,
            'indent': self.indent,
            'is_class': self.is_class,
            'is_function': self.is_function,
            'lines': self.lines,
            'name': self.name,
            'obj_type': self.obj_type,
            'parent_file_path': self.parent_file.path,
            'variables': self.variables,
            'returns': self.returns
        }
