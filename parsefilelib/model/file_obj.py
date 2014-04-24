from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.lib.file_obj import get_child_functions

class FileObj(object):
    """
    An object the encapsulates all details of a file
    """

    def __init__(self, file_path):
        """
        init method for the FileObj class
        """
        self.file_path = file_path
        self.file_lines = file_to_list(file_path)

    """ GETTERS """
    @property
    def child_functions(self):
        if hasattr(self, '_child_functions'):
            return self._child_functions

        self.child_functions = self.get_child_functions()

        return self.child_functions

    @property
    def file_lines(self):
        return self._file_lines

    @property
    def file_name(self):
        return self._file_path.split('/')[-1]

    @property
    def file_path(self):
        return self._file_path

    @property
    def num_lines(self):
        return len(self.file_lines)

    """ SETTERS """
    @child_functions.setter
    def child_functions(self, value):
        self._child_functions = value

    @file_lines.setter
    def file_lines(self, value):
        self._child_functions = value

    @file_lines.setter
    def file_lines(self, value):
        self._file_lines = value

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    """ GET FUNCTIONS """
    def get_child_functions(self):
        return get_child_functions(self.file_lines)
