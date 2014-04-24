try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os


class TestFolderObj(unittest.TestCase):
    def get_test_folder_path(self, folder_name):
        test_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
        return '%s/%s' %(test_dir, folder_name)
 
    def test_init__folder_path(self):
        from parsefilelib.model.folder_obj import FolderObj

        test_folder_path = self.get_test_folder_path('test_files')
        folder_obj = FolderObj(test_folder_path)

        assert folder_obj.folder_path == test_folder_path
 
    def test_init__folder_name(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        assert folder_obj.folder_name == folder_name
 
    def test_init__child_files__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_files) >= 5
 
    def test_init__child_files__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_files) == 1
 
    def test_init__child_files__tests(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_files) == 1
 
    #################################################################
    def test_init__child_folders__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folders) == 0
 
    def test_init__child_folders__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folders) == 2
 
    def test_init__child_folders__tests__length(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folders) == 3
 
    def test_init__child_folders__tests__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        for f in folder_obj.child_folders:
            if f.folder_name == 'unit':
                unit_folder  = f
                break

        # TODO: Put in a better check
        assert unit_folder.folder_name == 'unit'
        assert len(unit_folder.child_folders) == 2


    ################################################################
    def test_child_file_names__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_file_names) >= 5

    def test_child_file_names__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_file_names) == 1

    def test_child_file_names__tests(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_file_names) == 1


    ################################################################
    def test_child_folder_names__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folder_names) == 0

    def test_child_folder_names__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folder_names) == 2

    def test_child_folder_names__tests(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.child_folder_names) == 3


    ################################################################
    def test_is_module__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.is_module == False

    def test_child_folder_names__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.is_module == True

    def test_child_folder_names__tests(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.is_module == True


    ################################################################
    def test_rec_child_files__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_files) >= 5

    def test_rec_child_files__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_files) == 7

    def test_rec_child_files__tests(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_files) >= 14

    ################################################################
    def test_rec_child_folders__test_files(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_folders) == 0

    def test_rec_child_folders__unit(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'unit'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_folders) == 2

    def test_rec_child_folders__tests(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = ''
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert len(folder_obj.rec_child_folders) == 5

    ################################################################
    def test_single_child_mode__simple(self):
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        folder_obj = FolderObj(test_folder_path)

        # TODO: Put in a better check
        assert folder_obj.single_child_mode == False

    def test_single_child_mode__file_obj_created_first(self):
        from parsefilelib.model.file_obj import FileObj
        from parsefilelib.model.folder_obj import FolderObj

        folder_name = 'test_files'
        test_folder_path = self.get_test_folder_path(folder_name)
        test_file_path = "%s/%s" %(test_folder_path, 'simplest.py')
        file_obj = FileObj(test_file_path)
        folder_obj = FolderObj(test_folder_path, file_obj=file_obj)

        # TODO: Put in a better check
        assert folder_obj.single_child_mode == True
