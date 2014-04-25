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
 
    def test_init__lines(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.lines[0] == 'def foo():\n'
 
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

        assert file_obj.path == test_file_path

    ###########################################################
    def test_init__functions__simplest(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.functions
 
    def test_init__functions__simple_2(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple_2.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.functions) == 2
 
    def test_init__functions__simple_1(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.functions) == 7
 
    def test_init__functions__class_simple(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_simple.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.classes) == 1
        assert len(file_obj.functions) == 0
 
    def test_init__functions__class_with_extra_functions(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.classes) == 1
        assert len(file_obj.functions) == 1
        assert len(file_obj.classes[0].classes) == 0
        assert len(file_obj.classes[0].functions) == 2
        assert len(file_obj.functions[0].classes) == 0
        assert len(file_obj.functions[0].functions) == 0
 
    def test_init__functions__docstrings(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.functions) == 8

    ###########################################################
    def test_init__parent_folder(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.parent_folder.folder_name == 'test_files'

    ###########################################################
    ###########################################################
    ###########################################################
    def test_to_dict__simplest(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 0
        assert len(d['functions']) == 1
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 2
        assert d['name'] == 'simplest.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0

        assert len(d['functions'][0]['returns']) == 1
        assert d['functions'][0]['obj_type'] == 'function'
        assert d['functions'][0]['is_function'] == True
        assert d['functions'][0]['is_class'] == False
        assert d['functions'][0]['name'] == 'foo'

    def test_to_dict__simple_2(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple_2.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 0
        assert len(d['functions']) == 2
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 7
        assert d['name'] == 'simple_2.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0

        assert len(d['functions'][0]['returns']) == 1
        assert d['functions'][0]['obj_type'] == 'function'
        assert d['functions'][0]['is_function'] == True
        assert d['functions'][0]['is_class'] == False
        assert d['functions'][0]['name'] == 'first_function'

        assert len(d['functions'][1]['returns']) == 1
        assert len(d['functions'][1]['variables']) == 0
        assert d['functions'][1]['obj_type'] == 'function'
        assert d['functions'][1]['is_function'] == True
        assert d['functions'][1]['is_class'] == False
        assert d['functions'][1]['name'] == 'second_function'

    def test_to_dict__class_simple(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_simple.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 1
        assert len(d['functions']) == 0
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 10
        assert d['name'] == 'class_simple.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0
        
        assert len(d['classes'][0]['returns']) == 0
        assert d['classes'][0]['obj_type'] == 'class'
        assert d['classes'][0]['is_function'] == False
        assert d['classes'][0]['is_class'] == True
        assert d['classes'][0]['name'] == 'Foo'

        assert len(d['classes'][0]['functions'][0]['returns']) == 0
        assert len(d['classes'][0]['functions'][0]['variables']) == 1
        assert d['classes'][0]['functions'][0]['obj_type'] == 'function'
        assert d['classes'][0]['functions'][0]['is_function'] == True
        assert d['classes'][0]['functions'][0]['is_class'] == False
        assert d['classes'][0]['functions'][0]['name'] == '__init__'

    def test_to_dict__class_with_extra_function(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 1
        assert len(d['functions']) == 1
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 13
        assert d['name'] == 'class_with_extra_functions.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0
        
        assert len(d['classes'][0]['returns']) == 0
        assert d['classes'][0]['obj_type'] == 'class'
        assert d['classes'][0]['is_function'] == False
        assert d['classes'][0]['is_class'] == True
        assert d['classes'][0]['name'] == 'Foo'

        assert len(d['functions'][0]['returns']) == 1
        assert len(d['functions'][0]['variables']) == 0
        assert d['functions'][0]['obj_type'] == 'function'
        assert d['functions'][0]['is_function'] == True
        assert d['functions'][0]['is_class'] == False
        assert d['functions'][0]['name'] == 'extra'

    def test_to_dict__docstrings(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 0
        assert len(d['functions']) == 8
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 61
        assert d['name'] == 'docstrings.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0

        assert len(d['functions'][0]['returns']) == 1
        assert d['functions'][0]['obj_type'] == 'function'
        assert d['functions'][0]['is_function'] == True
        assert d['functions'][0]['is_class'] == False
        assert d['functions'][0]['name'] == 'first_docstring_function'

        assert len(d['functions'][6]['returns']) == 1
        assert len(d['functions'][6]['variables']) == 1
        assert d['functions'][6]['obj_type'] == 'function'
        assert d['functions'][6]['is_function'] == True
        assert d['functions'][6]['is_class'] == False
        assert d['functions'][6]['name'] == 'seventh_docstring_function'
        assert d['functions'][6]['docstrings'][0][1] == '    docstring with def in it\n'

        assert len(d['functions'][7]['returns']) == 1
        assert len(d['functions'][7]['variables']) == 1
        assert d['functions'][7]['obj_type'] == 'function'
        assert d['functions'][7]['is_function'] == True
        assert d['functions'][7]['is_class'] == False
        assert d['functions'][7]['name'] == 'eighth_docstring_function'
        assert d['functions'][7]['docstrings'][0][1] == 'docstring that is put all the way to the left\n'

    def test_to_dict__docstrings_def_left(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings_def_left.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 1
        assert len(d['functions']) == 0
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 13
        assert d['name'] == 'docstrings_def_left.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0
        
        assert len(d['classes'][0]['returns']) == 0
        assert len(d['classes'][0]['functions']) == 1
        assert d['classes'][0]['obj_type'] == 'class'
        assert d['classes'][0]['is_function'] == False
        assert d['classes'][0]['is_class'] == True
        assert d['classes'][0]['name'] == 'Foo'
        assert d['classes'][0]['docstrings'][0][1] == 'def hello():\n'

        assert len(d['classes'][0]['functions'][0]['returns']) == 1
        assert len(d['classes'][0]['functions'][0]['variables']) == 0
        assert d['classes'][0]['functions'][0]['obj_type'] == 'function'
        assert d['classes'][0]['functions'][0]['is_function'] == True
        assert d['classes'][0]['functions'][0]['is_class'] == False
        assert d['classes'][0]['functions'][0]['name'] == 'bar'
        assert d['classes'][0]['functions'][0]['docstrings'][0][1] == 'class Cool():\n'

    def test_to_dict__strings(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('strings.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 1
        assert len(d['functions']) == 0
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 22
        assert d['name'] == 'strings.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0
        
        assert len(d['classes'][0]['returns']) == 0
        assert len(d['classes'][0]['functions']) == 2
        assert d['classes'][0]['obj_type'] == 'class'
        assert d['classes'][0]['is_function'] == False
        assert d['classes'][0]['is_class'] == True
        assert d['classes'][0]['name'] == 'Foo'
        assert d['classes'][0]['docstrings'][0][1] == 'def hello():\n'

        assert len(d['classes'][0]['functions'][1]['returns']) == 1
        assert len(d['classes'][0]['functions'][1]['variables']) == 0
        assert d['classes'][0]['functions'][1]['obj_type'] == 'function'
        assert d['classes'][0]['functions'][1]['is_function'] == True
        assert d['classes'][0]['functions'][1]['is_class'] == False
        assert d['classes'][0]['functions'][1]['name'] == 'bar2'
        assert len(d['classes'][0]['functions'][1]['docstrings']) == 0

    def test_to_dict__decorators(self):
        from parsefilelib.model.file_obj import FileObj

        test_file_path = self.get_test_file_path('decorators.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 0
        assert len(d['functions']) == 3
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 0
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 15
        assert d['name'] == 'decorators.py'
        assert d['obj_type']  == 'file'
        assert len(d['returns']) == 0
        assert len(d['variables']) == 0
        
        assert len(d['functions'][0]['returns']) == 1
        assert len(d['functions'][0]['functions']) == 0
        assert len(d['functions'][0]['variables']) == 1
        assert len(d['functions'][0]['docstrings']) == 0
        assert len(d['functions'][0]['decorators']) == 0
        assert d['functions'][0]['obj_type'] == 'function'
        assert d['functions'][0]['is_function'] == True
        assert d['functions'][0]['is_class'] == False
        assert d['functions'][0]['name'] == 'foo'
        
        assert len(d['functions'][1]['returns']) == 1
        assert len(d['functions'][1]['functions']) == 0
        assert len(d['functions'][1]['variables']) == 1
        assert len(d['functions'][1]['docstrings']) == 0
        assert len(d['functions'][1]['decorators']) == 1
        assert d['functions'][1]['obj_type'] == 'function'
        assert d['functions'][1]['is_function'] == True
        assert d['functions'][1]['is_class'] == False
        assert d['functions'][1]['name'] == 'bar'
        
        assert len(d['functions'][2]['returns']) == 1
        assert len(d['functions'][2]['functions']) == 0
        assert len(d['functions'][2]['variables']) == 1
        assert len(d['functions'][2]['docstrings']) == 0
        assert len(d['functions'][2]['decorators']) == 3
        assert d['functions'][2]['obj_type'] == 'function'
        assert d['functions'][2]['is_function'] == True
        assert d['functions'][2]['is_class'] == False
        assert d['functions'][2]['name'] == 'foobar'
