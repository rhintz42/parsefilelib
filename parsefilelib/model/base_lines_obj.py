class BaseLineObj(object):
    """
    An object the encapsulates all details of a Lines object
    """

    # TODO: FUNCTION LINES MAYBE DANGEROUS
    #   Look into further to see best way to handle
    #   Do recursion in these files
    #       Check to make sure function_name is in there, though
    def __init__(self, obj_type, file_obj, name, lines=None):
        """
        init method for the BaseLineObj
        """
        self.parent_file = file_obj
        self.name = name
        self.obj_type = obj_type

        self.child_functions = []
        self.child_classes = []
        self.child_docstrings = []

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
    def child_functions(self):
        return self._child_functions

    @property
    def child_classes(self):
        return self._child_classes

    @property
    def child_docstrings(self):
        return self._child_docstrings

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

    @child_functions.setter
    def child_functions(self, value):
        self._child_functions = value

    @child_classes.setter
    def child_classes(self, value):
        self._child_classes = value

    @child_docstrings.setter
    def child_docstrings(self, value):
        self._child_docstrings = value

    #""" GET FUNCTIONS """

    """ APPEND FUNCTIONS """
    def append_child_function(self, func_obj):
        self._child_functions.append(func_obj)

    def append_child_class(self, class_obj):
        self._child_classes.append(class_obj)

    def append_child_docstring(self, docstring):
        self._child_docstrings.append(docstring)

    def append_child(self, obj):
        if obj.obj_type == 'function':
            self.append_child_function(obj)
        elif obj.obj_type == 'class':
            self.append_child_class(obj)
        else:
            self._child_docstrings.append(docstring)
