from parsefilelib.lib.parsefile import file_to_list
from parsefilelib.lib.file_obj import rec_fetch_children, \
                                      get_folder_path_from_file_path
from parsefilelib.models.base_lines_obj import BaseLinesObj

class FileObj(BaseLinesObj):
    """
    An object the encapsulates all details of a file
    """

    def __init__(self, path, parent_folder=None, lines=None):
        """
        init method for the FileObj class
        """
        self.path = path
        self.lines = file_to_list(path)
        
        # Init Parent Variables and Functions
        super(FileObj, self).__init__('file', self, self.file_name,
                                        lines=lines, indent=-1)

        # Get children
        self.fetch_children()

        # Get Parent
        if parent_folder:
            self.parent_folder = parent_folder
        else:
            from parsefilelib.models.folder_obj import FolderObj
            self.parent_folder = FolderObj(get_folder_path_from_file_path(path),
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
        self.functions = []
        self.classes = []
        self.docstrings = []

        rec_fetch_children(self, self, self.lines, -1, 0)

        return self.functions
    
    """ GET METHODS """
    def to_dict(self):
        parent_dict = super(FileObj, self).to_dict()
        # TODO: Add stuff only this class has to parent_dict
        return parent_dict
