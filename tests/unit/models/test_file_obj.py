try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os
from outlib.lib.wout import output_to_logger, output_to_file


class TestFileObj(unittest.TestCase):
    def get_test_file_path(self, file_name):
        test_files_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'test_files'))
        return '%s/%s' %(test_files_dir, file_name)
 
    def test_init__num_lines(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.num_lines == 2
 
    def test_init__lines(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.lines[0] == 'def foo():\n'
 
    def test_init__file_name(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_name = 'simplest.py'
        test_file_path = self.get_test_file_path(test_file_name)
        file_obj = FileObj(test_file_path)

        assert file_obj.file_name == test_file_name
 
    def test_init__file_path(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.path == test_file_path

    ###########################################################
    def test_init__functions__simplest(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.functions
 
    def test_init__functions__simple_2(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple_2.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.functions) == 2
 
    def test_init__functions__simple_1(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.functions) == 7
 
    def test_init__functions__class_simple(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_simple.py')
        file_obj = FileObj(test_file_path)

        #output_to_file('/opt/webapp/proflib_visualizer/src/proflib_visualizer/proflib_visualizer/static/json/parse_file_lib_json_files/test_1.json',
        #                [file_obj.to_dict()],
        #                append=False)

        assert len(file_obj.classes) == 1
        assert len(file_obj.functions) == 0
 
    def test_init__functions__class_with_extra_functions(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.classes) == 1
        assert len(file_obj.functions) == 1
        assert len(file_obj.classes[0].classes) == 0
        assert len(file_obj.classes[0].functions) == 2
        assert len(file_obj.functions[0].classes) == 0
        assert len(file_obj.functions[0].functions) == 0
 
    def test_init__functions__docstrings(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings.py')
        file_obj = FileObj(test_file_path)

        assert len(file_obj.functions) == 8

    ###########################################################
    def test_init__parent_folder(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(test_file_path)

        assert file_obj.parent_folder.name == 'test_files'

    ###########################################################
    ###########################################################
    ###########################################################
    def test_to_dict__simplest(self):
        from parsefilelib.models.file_obj import FileObj

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
        from parsefilelib.models.file_obj import FileObj

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
        from parsefilelib.models.file_obj import FileObj

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
        from parsefilelib.models.file_obj import FileObj

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
        from parsefilelib.models.file_obj import FileObj

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
        assert d['functions'][6]['docstring'] == 'docstring with def in it'

        assert len(d['functions'][7]['returns']) == 1
        assert len(d['functions'][7]['variables']) == 1
        assert d['functions'][7]['obj_type'] == 'function'
        assert d['functions'][7]['is_function'] == True
        assert d['functions'][7]['is_class'] == False
        assert d['functions'][7]['name'] == 'eighth_docstring_function'
        assert d['functions'][7]['docstring'] == 'docstring that is put all the way to the left'

    def test_to_dict__docstrings_def_left(self):
        from parsefilelib.models.file_obj import FileObj

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
        assert d['classes'][0]['docstring'] == 'def hello():\n    cool\n\ndef nice\n    '

        assert len(d['classes'][0]['functions'][0]['returns']) == 1
        assert len(d['classes'][0]['functions'][0]['variables']) == 0
        assert d['classes'][0]['functions'][0]['obj_type'] == 'function'
        assert d['classes'][0]['functions'][0]['is_function'] == True
        assert d['classes'][0]['functions'][0]['is_class'] == False
        assert d['classes'][0]['functions'][0]['name'] == 'bar'
        assert d['classes'][0]['functions'][0]['docstring'] == 'class Cool():\n        '

    def test_to_dict__strings(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('strings.py')
        file_obj = FileObj(test_file_path)

        d = file_obj.to_dict()

        assert len(d['classes']) == 1
        assert len(d['functions']) == 0
        assert d['parent_file_path'] == test_file_path
        assert len(d['imports']) == 4
        assert d['indent'] == -1
        assert d['is_class'] == False
        assert d['is_function'] == False
        assert len(d['lines']) == 24
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
        assert d['classes'][0]['docstring'] == 'def hello():\n    cool\n\ndef nice\n    '

        assert len(d['classes'][0]['functions'][1]['returns']) == 1
        assert len(d['classes'][0]['functions'][1]['variables']) == 0
        assert d['classes'][0]['functions'][1]['obj_type'] == 'function'
        assert d['classes'][0]['functions'][1]['is_function'] == True
        assert d['classes'][0]['functions'][1]['is_class'] == False
        assert d['classes'][0]['functions'][1]['name'] == 'bar2'
        assert d['classes'][0]['functions'][1]['docstring'] == None

    def test_to_dict__decorators(self):
        from parsefilelib.models.file_obj import FileObj

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
        assert len(d['functions'][0]['decorators']) == 0
        assert d['functions'][0]['docstring'] == None
        assert d['functions'][0]['obj_type'] == 'function'
        assert d['functions'][0]['is_function'] == True
        assert d['functions'][0]['is_class'] == False
        assert d['functions'][0]['name'] == 'foo'
        
        assert len(d['functions'][1]['returns']) == 1
        assert len(d['functions'][1]['functions']) == 0
        assert len(d['functions'][1]['variables']) == 1
        assert len(d['functions'][1]['decorators']) == 1
        assert d['functions'][1]['docstring'] == None
        assert d['functions'][1]['obj_type'] == 'function'
        assert d['functions'][1]['is_function'] == True
        assert d['functions'][1]['is_class'] == False
        assert d['functions'][1]['name'] == 'bar'
        
        assert len(d['functions'][2]['returns']) == 1
        assert len(d['functions'][2]['functions']) == 0
        assert len(d['functions'][2]['variables']) == 1
        assert len(d['functions'][2]['decorators']) == 3
        assert d['functions'][2]['docstring'] == None
        assert d['functions'][2]['obj_type'] == 'function'
        assert d['functions'][2]['is_function'] == True
        assert d['functions'][2]['is_class'] == False
        assert d['functions'][2]['name'] == 'foobar'


    ##################################################################
    ###################### ast_init ##################################
    ##################################################################
    def test_ast_init__simplest(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simplest.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 1
        assert len(file_obj.classes) == 0
        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 1

        assert file_obj.functions[0].line_index_start == 0
        assert file_obj.functions[0].line_index_end == 1

    def test_ast_init__simple_1(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple.py')
        file_obj = FileObj(file_path=test_file_path)

        #fi = open('/opt/webapp/parsefilelib/src/parsefilelib/test.py', 'w')
        #from parsefilelib.lib.unparse import Unparser
        #f = Unparser(file_obj.ast_node, file=fi);

        assert len(file_obj.functions) == 7
        assert len(file_obj.classes) == 0

        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 32

        assert file_obj.functions[0].line_index_start == 1
        assert file_obj.functions[0].line_index_end == 3

        assert file_obj.functions[1].line_index_start == 4
        assert file_obj.functions[1].line_index_end == 6

        assert file_obj.functions[2].line_index_start == 7
        assert file_obj.functions[2].line_index_end == 9

        assert file_obj.functions[3].line_index_start == 10
        assert file_obj.functions[3].line_index_end == 12

        assert file_obj.functions[4].line_index_start == 13
        assert file_obj.functions[4].line_index_end == 18

        assert file_obj.functions[5].line_index_start == 19
        assert file_obj.functions[5].line_index_end == 25

        assert file_obj.functions[6].line_index_start == 26
        assert file_obj.functions[6].line_index_end == 32

        assert len(file_obj.functions[6].returns) == 1
        assert len(file_obj.functions[6].variables) == 1

    def test_ast_init__simple_2(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('simple_2.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 2
        assert len(file_obj.classes) == 0

        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 6

        assert file_obj.functions[0].line_index_start == 1
        assert file_obj.functions[0].line_index_end == 3

        assert file_obj.functions[1].line_index_start == 4
        assert file_obj.functions[1].line_index_end == 6

    def test_ast_init__class_simple(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_simple.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 0
        assert len(file_obj.classes) == 1
        assert len(file_obj.classes[0].functions) == 2

        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 9

        assert file_obj.classes[0].line_index_start == 0
        assert file_obj.classes[0].line_index_end == 9

        assert file_obj.classes[0].functions[0].line_index_start == 5
        assert file_obj.classes[0].functions[0].line_index_end == 7

        assert file_obj.classes[0].functions[1].line_index_start == 8
        assert file_obj.classes[0].functions[1].line_index_end == 9

        assert len(file_obj.classes[0].functions[0].variables) == 1

    def test_ast_init__class_with_extra_functions(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 1
        assert len(file_obj.classes) == 1
        assert len(file_obj.classes[0].functions) == 2

        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 12

        assert file_obj.classes[0].line_index_start == 0
        assert file_obj.classes[0].line_index_end == 10

        assert file_obj.classes[0].functions[0].line_index_start == 5
        assert file_obj.classes[0].functions[0].line_index_end == 7

        assert file_obj.classes[0].functions[1].line_index_start == 8
        assert file_obj.classes[0].functions[1].line_index_end == 10

        assert file_obj.functions[0].line_index_start == 11
        assert file_obj.functions[0].line_index_end == 12

    def test_ast_init__docstrings(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 8
        assert len(file_obj.classes) == 0

        assert file_obj.functions[0].docstring == 'Single line docstring '
        assert file_obj.functions[1].docstring == '2 line docstring\n    '
        assert file_obj.functions[2].docstring == '2 line docstring part 2 '
        assert file_obj.functions[3].docstring == '3 line docstring'
        assert file_obj.functions[4].docstring == 'indented 3 line docstring'
        assert file_obj.functions[5].docstring == 'single quoted docstring'
        assert file_obj.functions[6].docstring == 'docstring with def in it'
        assert file_obj.functions[7].docstring == 'docstring that is put all the way to the left'

        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 60

        assert file_obj.functions[0].line_index_start == 1
        assert file_obj.functions[0].line_index_end == 4

        assert file_obj.functions[1].line_index_start == 5
        assert file_obj.functions[1].line_index_end == 9

        assert file_obj.functions[2].line_index_start == 10
        assert file_obj.functions[2].line_index_end == 14

        assert file_obj.functions[3].line_index_start == 15
        assert file_obj.functions[3].line_index_end == 20

        assert file_obj.functions[4].line_index_start == 21
        assert file_obj.functions[4].line_index_end == 29

        assert file_obj.functions[5].line_index_start == 30
        assert file_obj.functions[5].line_index_end == 39

        assert file_obj.functions[6].line_index_start == 40
        assert file_obj.functions[6].line_index_end == 50

        assert file_obj.functions[7].line_index_start == 51
        assert file_obj.functions[7].line_index_end == 60

    def test_ast_init__docstrings_def_left(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('docstrings_def_left.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 0
        assert len(file_obj.classes) == 1
        assert len(file_obj.classes[0].functions) == 1

        assert file_obj.classes[0].docstring == 'def hello():\n    cool\n\ndef nice\n    '
        assert file_obj.classes[0].functions[0].docstring == 'class Cool():\n        '


    def test_ast_init__decorators(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('decorators.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 3
        assert len(file_obj.classes) == 0

        assert file_obj.line_index_start == 0
        assert file_obj.line_index_end == 14

        assert file_obj.functions[0].line_index_start == 0
        assert file_obj.functions[0].line_index_end == 3

        assert file_obj.functions[1].line_index_start == 4
        assert file_obj.functions[1].line_index_end == 8

        assert file_obj.functions[2].line_index_start == 9
        assert file_obj.functions[2].line_index_end == 14

        assert len(file_obj.returns) == 0
        assert len(file_obj.functions[0].returns) == 1
        assert len(file_obj.functions[1].returns) == 1
        assert len(file_obj.functions[2].returns) == 1

        assert file_obj.functions[1].decorators[0].name == 'dec1'
        assert file_obj.functions[2].decorators[0].name == 'dec1'
        assert file_obj.functions[2].decorators[1].name == 'dec2'
        assert file_obj.functions[2].decorators[2].name == 'dec3'
        assert file_obj.functions[2].decorators[2].line_index_start == 11
        assert file_obj.functions[2].decorators[2].line_index_end == 12

        assert len(file_obj.functions[0].lines) == 4
        assert len(file_obj.functions[1].lines) == 5
        assert len(file_obj.functions[2].lines) == 6

    def test_ast_init__objects_1(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('objects_1.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 0
        assert len(file_obj.classes) == 1
        assert len(file_obj.classes[0].functions) == 3

    def test_ast_init__strings(self):
        from parsefilelib.models.file_obj import FileObj

        test_file_path = self.get_test_file_path('strings.py')
        file_obj = FileObj(file_path=test_file_path)

        assert len(file_obj.functions) == 0
        assert len(file_obj.classes) == 1
        assert len(file_obj.classes[0].functions) == 2

        assert file_obj.imports[3].level == 0
        assert file_obj.imports[3].module == 'parsefilelib.models.base_lines_obj'
        assert file_obj.imports[3].imps[0]['asname'] == None
        assert file_obj.imports[3].imps[0]['name'] == 'BaseLinesObj'
        assert file_obj.imports[3].imps[1]['asname'] == None
        assert file_obj.imports[3].imps[1]['name'] == 'node_type'
        assert file_obj.imports[3].imps[2]['asname'] == 'fetch_node'
        assert file_obj.imports[3].imps[2]['name'] == 'fetch_ast_node'

    ##########################################################################
    ######################## SURVEYMONKEY TEST FILES #########################
    ##########################################################################
    def test_ast_init__anweb_models_surveys(self):
        """
        These tests will fail unless the specific file is on your computer
            in the specific place indicated by `test_file_path`
        NOTE: This file is NOT static, thus this test is bound to fail over
            time. IF it fails, then check to make sure there isn't a bug in
            this project.
            * If there is a bug, then fix it and make this test
                passing.
            * If there is no bug, then just make this test pass again
        """
        from parsefilelib.models.file_obj import FileObj

        test_file_path = '/opt/webapp/anweb/src/anweb/anweb/models/surveys.py'
        file_obj = FileObj(file_path=test_file_path)
        output_to_file('/opt/webapp/proflib_visualizer/src/proflib_visualizer/proflib_visualizer/static/json/parse_file_lib_json_files/test_1.json',
                        [file_obj.to_dict()],
                        append=False)


        assert len(file_obj.functions) == 0
        assert len(file_obj.classes) == 4
        # file_obj.classes[2] should be the Survey class
        assert len(file_obj.classes[2].functions) == 87
        # file_obj.classes[3] should be the Page class
        assert len(file_obj.classes[3].functions) == 9
