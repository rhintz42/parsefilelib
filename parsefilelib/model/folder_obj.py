from parsefilelib.lib.folder_obj import get_child_file_names, \
                                        get_child_folder_names
from parsefilelib.model.file_obj import FileObj

class FolderObj(object):
    """
    An object the encapsulates all details of a Folder
    """

    def __init__(self, folder_path, parent_folder=None, file_obj=None, depth=None):
        """
        init method for the FileObj class
        """
        self.folder_path = folder_path

        self._child_files = []
        self._child_folders = []

        self.parent_folder = parent_folder

        self.fetch_child_file_objs(folder_path)
        self.fetch_child_folder_objs(folder_path)

    """ GETTERS """
    @property
    def child_files(self):
        return self._child_files

    @property
    def child_folders(self):
        return self._child_folders

    @property
    def child_file_names(self):
        return [ f.file_name for f in self.child_files ]

    @property
    def child_folder_names(self):
        return [ f.folder_name for f in self.child_folders ]

    @property
    def folder_name(self):
        return self._folder_path.split('/')[-1]

    @property
    def folder_path(self):
        return self._folder_path

    @property
    def is_module(self):
        for f in self.child_file_names:
            if f == '__init__.py':
                return True
        return False

    @property
    def parent_folder(self):
        return self._parent_folder

    @property
    def rec_child_files(self):
        pass

    @property
    def rec_child_folders(self):
        pass

    """ SETTERS """
    @folder_path.setter
    def folder_path(self, value):
        self._folder_path = value

    @parent_folder.setter
    def parent_folder(self, value):
        self._parent_folder = value

    """ APPENDERS """
    def append_child_file(self, value):
        self._child_files.append(value)

    def append_child_folder(self, value):
        self._child_folders.append(value)
    
    """ Fetch Methods """
    def fetch_child_file_objs(self, folder_path):
        child_file_names = get_child_file_names(folder_path)

        for c in child_file_names:
            file_path = '%s/%s' %(folder_path, c)
            self.append_child_file(FileObj(file_path, parent_folder=self))
        
        return self.child_files

    def fetch_child_folder_objs(self, folder_path):
        child_folder_names = get_child_folder_names(folder_path)

        for c in child_folder_names:
            f_path = '%s/%s' %(folder_path, c)
            self.append_child_folder(FolderObj(f_path, parent_folder=self))
        
        return self.child_folders
