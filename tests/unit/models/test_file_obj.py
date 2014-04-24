try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os


class TestFileObj(unittest.TestCase):
    def get_test_file_path(self, file_name):
        test_files_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'test_files'))
        return '%s/%s' %(test_files_dir, file_name)
 
    def test_init__num_lines(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.num_lines == 2
 
    def test_init__file_lines(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.file_lines[0] == 'def foo():\n'
 
    def test_init__file_name(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_name = 'simplest.py'
        test_file_path = self.get_test_file_path(test_file_name)
        file_obj = FileObj(test_file_path)

        assert file_obj.file_name == test_file_name
 
    def test_init__file_path(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.file_path == test_file_path

    ###########################################################
    def test_init__child_functions__simplest(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.child_functions
 
    def test_init__child_functions__simple_2(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple_2.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.child_functions) == 2
 
    def test_init__child_functions__simple_1(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.child_functions) == 7
 
    def test_init__child_functions__class_simple(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_simple.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.child_classes) == 1
        assert len(file_obj.child_functions) == 0
 
    def test_init__child_functions__class_with_extra_functions(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.child_classes) == 1
        assert len(file_obj.child_functions) == 1
        assert len(file_obj.child_classes[0].child_classes) == 0
        assert len(file_obj.child_classes[0].child_functions) == 2
        assert len(file_obj.child_functions[0].child_classes) == 0
        assert len(file_obj.child_functions[0].child_functions) == 0
 
    def test_init__child_functions__docstrings(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.child_functions) == 8

    ###########################################################
    def test_init__parent_folder(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.parent_folder.folder_name == 'test_files'
