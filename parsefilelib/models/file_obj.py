from parsefilelib.lib.file_obj import get_folder_path_from_file_path
from parsefilelib.models.base_lines_obj import BaseLinesObj

class FileObj(BaseLinesObj):
    """
    An object that encapsulates all details of a file
    """

    def __init__(self, file_path=None, parent_folder=None, lines=None,
                    child=None):
        """
        init method for the FileObj class

        the optional stuff:
        * child_function: If you are just creating a function, and don't want
            to grab all the children of a file, then this will just use your 
            specific function as the children
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
    def name(self):
        """
        Return the name of this file
        """
        return self._path.split('/')[-1]

    @property
    def parent_folder(self):
        """
        Return the parent of this file
        """
        return self._parent_folder

    @property
    def path(self):
        """
        Return the path of this file
        """
        return self._path


    """ SETTERS """

    @parent_folder.setter
    def parent_folder(self, value):
        """
        Set the _parent_folder property of this file
        """
        self._parent_folder = value

    @path.setter
    def path(self, value):
        """
        Set the _path property of this file
        """
        self._path = value


    """ FETCH CHILD OBJECTS """

    def fetch_children(self):
        """
        Return the child functions and classes of this file
        """
        # TODO: Tests
        self.docstrings = []
        return self.functions + self.classes

    
    """ GET METHODS """

    def to_dict(self):
        """
        Returns a dictionary representation of this File
        """
        parent_dict = super(FileObj, self).to_dict()
        # TODO: Add stuff only this class has to parent_dict
        return parent_dict
