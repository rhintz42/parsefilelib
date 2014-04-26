try:
    import unittest2 as unittest
except:
    import unittest
import sys
import os


class TestFuncObj(unittest.TestCase):
    def get_test_file_path(self, file_name):
        test_files_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'test_files'))
        return '%s/%s' %(test_files_dir, file_name)
 
    def test_func_init__simplest(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simplest.py')
        func_obj = BaseLinesObj(file_path=test_file_path, def_name='foo')

        assert len(func_obj.lines) == 2
        assert func_obj.returns[0].value == 'bar'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'foo'
        assert p_d['name'] == 'simplest.py'
        assert p_fd['name'] == 'simplest.py'
 
    def test_func_init__simple_1__first_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='first_function')

        assert len(func_obj.lines) == 3
        assert func_obj.returns[0].value == 'first_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'first_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
 
    def test_func_init__simple_1__second_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='second_function')

        assert len(func_obj.lines) == 3
        assert func_obj.returns[0].value == 'second_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'second_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
 
    def test_func_init__simple_1__third_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='third_function')

        assert len(func_obj.lines) == 3
        assert func_obj.returns[0].value == 'third_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'third_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
 
    def test_func_init__simple_1__fourth_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='fourth_function')

        assert len(func_obj.lines) == 3
        assert func_obj.returns[0].value == 'fourth_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'fourth_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
 
    def test_func_init__simple_1__fifth_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='fifth_function')

        assert len(func_obj.lines) == 6
        assert func_obj.returns[0].value == '\n        fifth_function_return\n    '

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'fifth_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
 
    def test_func_init__simple_1__sixth_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='sixth_function')

        assert len(func_obj.lines) == 7
        assert func_obj.variables[0].target == 'b'
        assert func_obj.variables[0].value == 20
        assert func_obj.variables[1].target == 'c'
        assert func_obj.variables[1].value == 30
        assert func_obj.returns[0].value == '\n        sixth_function_return\n    '

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'sixth_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
 
    def test_func_init__simple_1__seventh_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='seventh_function')

        assert len(func_obj.lines) == 7
        assert func_obj.returns[0].value == '\n\n        sixth_function_return\n\n    '

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'seventh_function'
        assert p_d['name'] == 'simple.py'
        assert p_fd['name'] == 'simple.py'
