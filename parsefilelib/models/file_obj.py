from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.lib.file_obj import get_folder_path_from_file_path
from parsefilelib.models.base_lines_obj import BaseLinesObj

class FileObj(BaseLinesObj):
    """
    An object the encapsulates all details of a file
    """

    def __init__(self, file_path=None, parent_folder=None, lines=None,
                    child=None):
        """
        init method for the FileObj class

        the optional stuff:
        * child_function: If you are just creating a function, and don't want
            to grab all the children, then this will just use your specific
            function as the children
            NOTE: You can still grab all the files children recursively
        """
        self.path = file_path
        self.functions = []
        self.classes = []
        
        # Init Parent Variables and Functions
        if child:
            self.append_child(child)
            super(FileObj, self).__init__(file_path=file_path, parent_file=self,
                                            file_lines=lines, indent=-1,
                                            get_children=False)
        else:
            super(FileObj, self).__init__(file_path=file_path, parent_file=self,
                                            file_lines=lines, indent=-1,
                                            get_children=True)

        # Get Parent
        if parent_folder:
            self.parent_folder = parent_folder
        else:
            from parsefilelib.models.folder_obj import FolderObj
            self.parent_folder = FolderObj(get_folder_path_from_file_path(file_path),
                                           file_obj=self)

    """ GETTERS """
    @property
    def file_name(self):
        return self._path.split('/')[-1]

    @property
    def path(self):
        return self._path

    @property
    def parent_folder(self):
        return self._parent_folder

    """ SETTERS """
    @parent_folder.setter
    def parent_folder(self, value):
        self._parent_folder = value

    @path.setter
    def path(self, value):
        self._path = value

    """ APPEND FUNCTIONS """

    """ FETCH CHILD OBJECTS """
    def fetch_children(self):
        self.docstrings = []


        return self.functions
    
    """ GET METHODS """
    def to_dict(self):
        parent_dict = super(FileObj, self).to_dict()
        # TODO: Add stuff only this class has to parent_dict
        return parent_dict
