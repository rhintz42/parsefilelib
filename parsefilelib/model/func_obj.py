class FuncObj(object):
    """
    An object the encapsulates all details of a function
    """

    def __init__(self, file_obj, function_name):
        """
        init method for the FileObj class
        """
        self.parent_file_obj = file_obj
        # Get the function lines from the file_lines

    """ GETTERS """
    @property
    def parent_file_obj(self):
        return self._parent_file_obj

    @property
    def function_name(self):
        return self._function_name

    @property
    def function_lines(self):
        return self._function_lines

    """ SETTERS """
    @parent_file_obj.setter
    def parent_file_obj(self, value):
        self._parent_file_obj = value

    @function_name.setter
    def function_name(self, value):
        self._function_name = value

    @function_lines.setter
    def function_lines(self, value):
        self._function_lines = value

    #""" GET FUNCTIONS """
