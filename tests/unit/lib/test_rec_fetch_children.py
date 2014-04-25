try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os


class TestRecFetchChildren(unittest.TestCase):
    def get_test_file_path(self, file_name):
        test_files_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'test_files'))
        return '%s/%s' %(test_files_dir, file_name)
    
    def test_rec_fetch_children__simplest(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 0
        assert len(file_obj.child_functions) == 1
        assert len(file_obj.child_docstrings) == 0
 
    def test_rec_fetch_children__simple_1(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 0
        assert len(file_obj.child_functions) == 7
        assert len(file_obj.child_docstrings) == 0
 
    def test_rec_fetch_children__simple_2(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple_2.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 0
        assert len(file_obj.child_functions) == 2
        assert len(file_obj.child_docstrings) == 0
 
    def test_rec_fetch_children__class_simple(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_simple.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []
        file_obj.child_docstrings = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 1
        assert len(file_obj.child_functions) == 0
        assert len(file_obj.child_classes[0].child_classes) == 0
        assert len(file_obj.child_classes[0].child_functions) == 2
        assert len(file_obj.child_classes[0].child_docstrings) == 1
 
    def test_rec_fetch_children__class_with_extra_functions(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 1
        assert len(file_obj.child_functions) == 1
        assert len(file_obj.child_classes[0].child_classes) == 0
        assert len(file_obj.child_classes[0].child_functions) == 2

    def test_rec_fetch_children__docstrings(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 0
        assert len(file_obj.child_functions) == 8

    def test_rec_fetch_children__strings(self):
        from parsefilelib.lib.file_obj import rec_fetch_children
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('strings.py')
        file_obj = FileObj(test_file_path)

        # Reset child arrays
        file_obj.child_functions = []
        file_obj.child_classes = []

        end_i = rec_fetch_children(file_obj, file_obj, file_obj.file_lines, -1, 0)

        assert len(file_obj.child_classes) == 1
        assert len(file_obj.child_functions) == 0
        assert len(file_obj.child_classes[0].child_functions) == 2
