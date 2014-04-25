class BaseLinesObj(object):
    """
    An object the encapsulates all details of a Lines object
    """

    # TODO: FUNCTION LINES MAYBE DANGEROUS
    #   Look into further to see best way to handle
    #   Do recursion in these files
    #       Check to make sure function_name is in there, though
    def __init__(self, obj_type, file_obj, name, lines=None):
        """
        init method for the BaseLinesObj
        """
        self.parent_file = file_obj
        self.name = name
        self.obj_type = obj_type

        self.functions = []
        self.classes = []
        self.docstrings = []
        self.comments = []
        self.imports = []
        self.variables = []
        self.returns = []
        self.decorators = []

        if lines:
            self.lines = lines

    """ GETTERS """
    @property
    def parent_file(self):
        return self._parent_file

    @property
    def name(self):
        return self._name

    @property
    def lines(self):
        return self._lines

    @property
    def obj_type(self):
        return self._obj_type

    @property
    def is_class(self):
        return self._obj_type == 'class'

    @property
    def is_function(self):
        return self._obj_type == 'function'

    @property
    def functions(self):
        return self._functions

    @property
    def classes(self):
        return self._classes

    @property
    def docstrings(self):
        return self._docstrings

    @property
    def comments(self):
        return self._comments

    @property
    def imports(self):
        return self._imports

    @property
    def variables(self):
        return self._variables

    @property
    def returns(self):
        return self._returns

    @property
    def decorators(self):
        return self._decorators

    """ SETTERS """
    @parent_file.setter
    def parent_file(self, value):
        self._parent_file = value

    @name.setter
    def name(self, value):
        self._name = value

    @lines.setter
    def lines(self, value):
        self._lines = value

    @obj_type.setter
    def obj_type(self, value):
        self._obj_type = value

    @functions.setter
    def functions(self, value):
        self._functions = value

    @classes.setter
    def classes(self, value):
        self._classes = value

    @docstrings.setter
    def docstrings(self, value):
        self._docstrings = value

    @comments.setter
    def comments(self, value):
        self._comments = value

    @imports.setter
    def imports(self, value):
        self._imports = value

    @variables.setter
    def variables(self, value):
        self._variables = value

    @returns.setter
    def returns(self, value):
        self._returns = value

    @decorators.setter
    def decorators(self, value):
        self._decorators = value

    """ APPEND FUNCTIONS """
    def append_function(self, func_obj):
        self._functions.append(func_obj)

    def append_class(self, class_obj):
        self._classes.append(class_obj)

    def append_docstring(self, docstring):
        self._docstrings.append(docstring)

    def append_comment(self, comment):
        self._comments.append(comment)

    def append_import(self, imp):
        self._imports.append(imp)

    def append_variable(self, v):
        self._variables.append(v)

    def append_return(self, ret):
        self._returns.append(ret)

    def append_decorator(self, decorator):
        self._decorators.append(decorator)

    def append_child(self, obj):
        if obj.obj_type == 'function':
            self.append_function(obj)
        elif obj.obj_type == 'class':
            self.append_class(obj)
        else:
            self._docstrings.append(docstring)
