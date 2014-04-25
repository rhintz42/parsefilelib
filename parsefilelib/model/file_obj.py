from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.lib.file_obj import rec_fetch_children, \
                                      get_folder_path_from_file_path

class FileObj(object):
    """
    An object the encapsulates all details of a file
    """

    def __init__(self, path, parent_folder=None):
        """
        init method for the FileObj class
        """
        self.path = path
        self.file_lines = file_to_list(path)
        self.obj_type = 'file'

        self.functions = []
        self.classes = []
        self.docstrings = []
        self.comments = []
        self.imports = []
        self.variables = []
        self.returns = []
        self.decorators = []

        self.fetch_children()

        if parent_folder:
            self.parent_folder = parent_folder
        else:
            from parsefilelib.model.folder_obj import FolderObj
            self.parent_folder = FolderObj(get_folder_path_from_file_path(path),
                                           file_obj=self)

    """ GETTERS """
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

    @property
    def obj_type(self):
        return self._obj_type

    @property
    def file_lines(self):
        return self._file_lines

    @property
    def file_name(self):
        return self._path.split('/')[-1]

    @property
    def path(self):
        return self._path

    @property
    def parent_folder(self):
        return self._parent_folder

    @property
    def num_lines(self):
        return len(self.file_lines)

    """ SETTERS """
    @functions.setter
    def functions(self, value):
        self._functions = value

    @classes.setter
    def classes(self, value):
        self._classes = value

    @docstrings.setter
    def docstrings(self, value):
        self._docstrings = value

    @file_lines.setter
    def file_lines(self, value):
        self._file_lines = value

    @path.setter
    def path(self, value):
        self._path = value

    @obj_type.setter
    def obj_type(self, value):
        self._obj_type = value

    @parent_folder.setter
    def parent_folder(self, value):
        self._parent_folder = value

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

    def append_return(self, v):
        self._returns.append(v)

    def append_decorator(self, decorator):
        self._decorators.append(decorator)

    def append_child(self, obj):
        if obj.obj_type == 'function':
            self.append_function(obj)
        elif obj.obj_type == 'class':
            self.append_class(obj)
        else:
            self._docstrings.append(docstring)

    """ FETCH CHILD OBJECTS """
    def fetch_children(self):
        self.functions = []
        self.classes = []
        self.docstrings = []

        rec_fetch_children(self, self, self.file_lines, -1, 0)

        return self.functions
        
