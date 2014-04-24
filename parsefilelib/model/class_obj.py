class ClassObj(object):
    """
    An object the encapsulates all details of a class

    SHOULD MERGE THIS CLASS WITH FuncObj BECAUSE SOO SIMILAR
    * CREATE A BASE CLASS THAT CAN INHERIT FROM
    """

    # TODO: FUNCTION LINES MAYBE DANGEROUS
    #   Look into further to see best way to handle
    #   Do recursion in these files
    #       Check to make sure function_name is in there, though
    def __init__(self, file_obj, name, lines=None):
        """
        init method for the FileObj class
        """
        self.parent_file = file_obj
        self.name = name

        self.child_functions = []
        self.child_classes = []

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
    def child_functions(self):
        return self._child_functions

    @property
    def child_classes(self):
        return self._child_classes

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

    @child_functions.setter
    def child_functions(self, value):
        self._child_functions = value

    @child_classes.setter
    def child_classes(self, value):
        self._child_classes = value

    #""" GET FUNCTIONS """

    """ APPEND FUNCTIONS """
    def append_child_function(self, func_obj):
        self._child_functions.append(func_obj)

    def append_child_class(self, class_obj):
        self._child_classes.append(class_obj)
