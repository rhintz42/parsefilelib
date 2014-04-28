from parsefilelib.lib.folder_obj import get_child_file_names, \
                                        get_child_folder_names, \
                                        format_folder_path
from parsefilelib.models.file_obj import FileObj

class FolderObj(object):
    """
    An object the encapsulates all details of a Folder
    """

    def __init__(self, folder_path, parent_folder=None, file_obj=None,
                    depth=None):
        """
        init method for the FileObj class
        """
        self.path = format_folder_path(folder_path)

        self.files = []
        self.folders = []

        self.parent_folder = parent_folder

        if file_obj:
            self.single_child_mode = True
            self.append_child_file(file_obj)
        else:
            self.files = self.fetch_child_file_objs(folder_path)
            self.folders = self.fetch_child_folder_objs(folder_path)

    """ GETTERS """

    @property
    def files(self):
        """
        Return the files in this folder
        """
        return self._files

    @property
    def folders(self):
        """
        Return the folders in this folder

        If this object is set to `single_child_mode`, then this will return an
            empty array
        """
        return self._folders

    @property
    def children(self):
        """
        Return all of the objects in this folder, which consists of both files
            and folders

        If this object is set to `single_child_mode`, then this will return the
            same array that self.files returns
        """
        return self.folders + self.files

    @property
    def child_file_names(self):
        """
        Return an array of all of the file names in this folder

        If this object is set to `single_child_mode`, then this will return an
            array with only the name of the only file given to this object
        """
        return [ f.name for f in self.files ]

    @property
    def child_folder_names(self):
        """
        Return an array of all of the folder names in this folder

        If this object is set to `single_child_mode`, then this will return an
            empty array
        """
        return [ f.name for f in self.folders ]

    @property
    def name(self):
        """
        Return the name of this folder
        """
        return self.path.split('/')[-2]

    @property
    def path(self):
        """
        Return the path of this folder
        """
        return self._path

    @property
    def is_module(self):
        """
        Return whether this folder is a module or not
        """
        for f in self.child_file_names:
            if f == '__init__.py':
                return True
        return False

    @property
    def parent_folder(self):
        """
        Return the parent of this folder
        """
        return self._parent_folder

    @property
    def rec_child_files(self):
        """
        Return ALL the files under this folder, including files within the
        child folders of this folder and so on
        """
        c_files = self.files
        
        for f in self.folders:
            c_files += f.rec_child_files

        return c_files

    @property
    def rec_child_folders(self):
        """
        Return ALL the folders under this folder, including files within the
        child folders of this folder and so on
        """
        c_folders = self.folders

        for f in self.folders:
            c_folders += f.rec_child_folders

        return c_folders

    @property
    def single_child_mode(self):
        """
        Return whether this folder is tied to a single child file or not

        Reasons this would be true is if you created a FuncObj that is tied to
            a frame and you wanted to just tie that to a file, then tie that
            file to a folder
        """
        return self._single_child_mode

    """ SETTERS """

    @files.setter
    def files(self, value):
        """
        Set the _files property of this folder
        """
        self._files = value

    @folders.setter
    def folders(self, value):
        """
        Set the _folders property of this folder
        """
        self._folders = value

    @path.setter
    def path(self, value):
        """
        Set the _path property of this folder
        """
        self._path = value

    @parent_folder.setter
    def parent_folder(self, value):
        """
        Set the _parent_folder property of this folder
        """
        self._parent_folder = value

    @single_child_mode.setter
    def single_child_mode(self, value):
        """
        Set the _single_child_mode property of this folder
        """
        self._single_child_mode = value

    """ APPENDERS """

    def append_child_file(self, value):
        """
        Append a file to the files property of this folder
        """
        self.files.append(value)

    def append_child_folder(self, value):
        """
        Append a folder to the folders property of this folder
        """
        self.folders.append(value)
    
    """ Fetch Methods """

    def fetch_child_file_objs(self, folder_path):
        """
        Return the files in this folder

        Note about single_child_mode: This method disregards single child mode
            and will return ALL of the files in this folder
        """
        self.single_child_mode = False
        child_file_names = get_child_file_names(folder_path)
        child_files = []

        for c in child_file_names:
            file_path = '%s%s' %(folder_path, c)
            child_files.append(FileObj(file_path, parent_folder=self))
        
        return child_files

    def fetch_child_folder_objs(self, folder_path):
        """
        Return the folders in this folder

        Note about single_child_mode: This method disregards single child mode
            and will return ALL of the folders in this folder
        """
        child_folder_names = get_child_folder_names(folder_path)
        child_folders = []

        for c in child_folder_names:
            f_path = '%s%s/' %(folder_path, c)
            child_folders.append(FolderObj(f_path, parent_folder=self))
        
        return child_folders

    """ GET METHODS """

    def to_dict(self):
        """
        Returns ...

        Stuff to note:
        * Don't print parent because we don't want to have a circular thing
            going
        * Don't need num_lines, kind of pointless for others because they have
            access to lines and the python library
        """
        return {
            'files': [f.to_dict() for f in self.files],
            'folders': [f.to_dict() for f in self.folders],
            'children': [c.to_dict() for c in self.children],
            'folder_path': self.path,
            'name': self.name,
        }
