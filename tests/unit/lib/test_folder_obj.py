try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os


class TestLibFolderObj(unittest.TestCase):
    def get_test_folder_path(self, folder_name):
        test_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
        return '%s/%s' %(test_dir, folder_name)
    
    def test_get_child_file_names__test_files(self):
        from parsefilelib.lib.folder_obj import get_child_file_names

        test_files_dir = self.get_test_folder_path('test_files')
        file_names = get_child_file_names(test_files_dir)

        assert 'simple.py' in file_names
    
    def test_get_child_folder_names__test_files(self):
        from parsefilelib.lib.folder_obj import get_child_folder_names

        test_files_dir = self.get_test_folder_path('test_files')
        folder_names = get_child_folder_names(test_files_dir)

        assert folder_names == []
    
    def test_get_child_folder_names__unit(self):
        from parsefilelib.lib.folder_obj import get_child_folder_names

        test_files_dir = self.get_test_folder_path('unit')
        folder_names = get_child_folder_names(test_files_dir)

        assert 'lib' in folder_names
        assert 'models' in folder_names
        assert '__init__.py' not in folder_names

