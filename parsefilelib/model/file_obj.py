from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.lib.file_obj import rec_fetch_children, \
                                      get_folder_path_from_file_path

class FileObj(object):
    """
    An object the encapsulates all details of a file
    """

    def __init__(self, file_path, parent_folder=None):
        """
        init method for the FileObj class
        """
        self.file_path = file_path
        self.file_lines = file_to_list(file_path)

        self.child_functions = []
        self.child_classes = []
        self.child_docstrings = []

        self.fetch_children()

        if parent_folder:
            self.parent_folder = parent_folder
        else:
            from parsefilelib.model.folder_obj import FolderObj
            self.parent_folder = FolderObj(get_folder_path_from_file_path(file_path),
                                           file_obj=self)

    """ GETTERS """
    @property
    def child_functions(self):
        return self._child_functions

    @property
    def child_classes(self):
        return self._child_classes

    @property
    def child_docstrings(self):
        return self._child_docstrings

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
    def parent_folder(self):
        return self._parent_folder

    @property
    def num_lines(self):
        return len(self.file_lines)

    """ SETTERS """
    @child_functions.setter
    def child_functions(self, value):
        self._child_functions = value

    @child_classes.setter
    def child_classes(self, value):
        self._child_classes = value

    @child_docstrings.setter
    def child_docstrings(self, value):
        self._child_docstrings = value

    @file_lines.setter
    def file_lines(self, value):
        self._file_lines = value

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    @parent_folder.setter
    def parent_folder(self, value):
        self._parent_folder = value

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

    """ FETCH CHILD OBJECTS """
    def fetch_children(self):
        self.child_functions = []
        self.child_classes = []
        self.child_docstrings = []

        rec_fetch_children(self, self, self.file_lines, -1, 0)

        return self.child_functions
        
