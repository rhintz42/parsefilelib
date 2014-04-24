try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os


class TestParseFile(unittest.TestCase):
    def get_test_file_path(self, file_name):
        test_files_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'test_files'))
        return '%s/%s' %(test_files_dir, file_name)
    
    def test_file_to_list__simplest(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('simplest.py')
        file_list = file_to_list(test_file)

        assert file_list[0] == 'def foo():\n'
    
    def test_file_to_list__simplest__length(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('simplest.py')
        file_list = file_to_list(test_file)

        assert len(file_list) == 2
    
    def test_file_to_list__simple(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('simple.py')
        file_list = file_to_list(test_file)

        assert file_list[1] == 'def first_function():\n'
    
    def test_file_to_list__simple__length(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('simple.py')
        file_list = file_to_list(test_file)

        assert len(file_list) == 33
    
    def test_file_to_list__docstrings(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('docstrings.py')
        file_list = file_to_list(test_file)

        assert file_list[1] == 'def first_docstring_function():\n'
    
    def test_file_to_list__docstrings__length(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('docstrings.py')
        file_list = file_to_list(test_file)

        assert len(file_list) == 50
    
    def test_file_to_list__class_simple(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('class_simple.py')
        file_list = file_to_list(test_file)

        assert file_list[0] == 'class Foo(object):\n'
    
    def test_file_to_list__class_simple__length(self):
        from parsefilelib.lib.parsefile import file_to_list

        test_file = self.get_test_file_path('class_simple.py')
        file_list = file_to_list(test_file)

        assert len(file_list) == 10
