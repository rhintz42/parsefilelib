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
 
    def test_func_init__simple_2__first_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple_2.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='first_function')

        assert len(func_obj.lines) == 3
        assert func_obj.returns[0].value == 'first_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'first_function'
        assert p_d['name'] == 'simple_2.py'
        assert p_fd['name'] == 'simple_2.py'
 
    def test_func_init__simple_2__second_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('simple_2.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='second_function')

        assert len(func_obj.lines) == 3
        assert func_obj.returns[0].value == 'second_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'second_function'
        assert p_d['name'] == 'simple_2.py'
        assert p_fd['name'] == 'simple_2.py'
 
    def test_func_init__class_simple__foo_class(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('class_simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='Foo')

        assert len(func_obj.lines) == 10

        d = func_obj.to_dict()
        # TODO: EVENTUALLY MAKE THE PARENT OBJ THE ACTUAL PARENT OBJ.
        #       * In this case, it'd be the class `Foo`
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'Foo'
        assert p_d['name'] == 'class_simple.py'
        assert p_fd['name'] == 'class_simple.py'
 
    def test_func_init__class_simple__init_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('class_simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='__init__')

        assert len(func_obj.lines) == 3
        assert func_obj.variables[0].value == 20

        d = func_obj.to_dict()
        # TODO: EVENTUALLY MAKE THE PARENT OBJ THE ACTUAL PARENT OBJ.
        #       * In this case, it'd be the class `Foo`
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == '__init__'
        assert p_d['name'] == 'class_simple.py'
        assert p_fd['name'] == 'class_simple.py'
 
    def test_func_init__class_simple__bar_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('class_simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='bar')

        assert len(func_obj.lines) == 2
        assert func_obj.returns[0].value == 'hello'

        d = func_obj.to_dict()
        # TODO: EVENTUALLY MAKE THE PARENT OBJ THE ACTUAL PARENT OBJ.
        #       * In this case, it'd be the class `Foo`
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'bar'
        assert p_d['name'] == 'class_simple.py'
        assert p_fd['name'] == 'class_simple.py'
 
    def test_func_init__class_with_extra_functions__extra_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('class_with_extra_functions.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='extra')

        assert len(func_obj.lines) == 2
        assert func_obj.returns[0].value == 'extra function'

        d = func_obj.to_dict()
        # TODO: EVENTUALLY MAKE THE PARENT OBJ THE ACTUAL PARENT OBJ.
        #       * In this case, it'd be the class `Foo`
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'extra'
        assert p_d['name'] == 'class_with_extra_functions.py'
        assert p_fd['name'] == 'class_with_extra_functions.py'
 
    def test_func_init__compare_conditions_simple__if_statement(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('compare_conditions_simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='if_statement')

        assert len(func_obj.lines) == 5
        assert func_obj.returns[0].value == 30

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'if_statement'
        assert p_d['name'] == 'compare_conditions_simple.py'
        assert p_fd['name'] == 'compare_conditions_simple.py'
 
    def test_func_init__compare_conditions_simple__for_loop(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('compare_conditions_simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='for_loop')

        assert len(func_obj.lines) == 7
        assert len(func_obj.returns) == 0

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'for_loop'
        assert p_d['name'] == 'compare_conditions_simple.py'
        assert p_fd['name'] == 'compare_conditions_simple.py'
 
    def test_func_init__compare_conditions_simple__while_loop(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('compare_conditions_simple.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='while_loop')

        assert len(func_obj.lines) == 4
        assert len(func_obj.returns) == 0

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'while_loop'
        assert p_d['name'] == 'compare_conditions_simple.py'
        assert p_fd['name'] == 'compare_conditions_simple.py'

 
    def test_func_init__decorators__foo(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('decorators.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='foo')

        assert len(func_obj.lines) == 4
        assert len(func_obj.decorators) == 0
        assert func_obj.returns[0].value == 20

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'foo'
        assert p_d['name'] == 'decorators.py'
        assert p_fd['name'] == 'decorators.py'

    def test_func_init__decorators__bar(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('decorators.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='bar')

        assert len(func_obj.lines) == 5
        assert func_obj.decorators[0].name == 'dec1'
        assert func_obj.returns[0].value == 30

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'bar'
        assert p_d['name'] == 'decorators.py'
        assert p_fd['name'] == 'decorators.py'

    def test_func_init__decorators__foobar(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('decorators.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='foobar')

        assert len(func_obj.lines) == 6
        assert func_obj.decorators[0].name == 'dec1'
        assert func_obj.decorators[1].name == 'dec2'
        assert func_obj.decorators[2].name == 'dec3'
        assert func_obj.returns[0].value == 'k'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'foobar'
        assert p_d['name'] == 'decorators.py'
        assert p_fd['name'] == 'decorators.py'


    def test_func_init__docstrings__first_docstring_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('docstrings.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='first_docstring_function')

        assert len(func_obj.lines) == 4
        assert func_obj.docstring == 'Single line docstring '
        assert func_obj.returns[0].value == 'first_docstring_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'first_docstring_function'
        assert p_d['name'] == 'docstrings.py'
        assert p_fd['name'] == 'docstrings.py'

    def test_func_init__docstrings__second_docstring_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('docstrings.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='second_docstring_function')

        assert len(func_obj.lines) == 5
        assert func_obj.docstring == '2 line docstring\n    '
        assert func_obj.returns[0].value == 'second_docstring_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'second_docstring_function'
        assert p_d['name'] == 'docstrings.py'
        assert p_fd['name'] == 'docstrings.py'

    def test_func_init__docstrings__third_docstring_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('docstrings.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='third_docstring_function')

        assert len(func_obj.lines) == 5
        assert func_obj.docstring == '2 line docstring part 2 '
        assert func_obj.returns[0].value == 'third_docstring_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'third_docstring_function'
        assert p_d['name'] == 'docstrings.py'
        assert p_fd['name'] == 'docstrings.py'

    def test_func_init__docstrings__fourth_docstring_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('docstrings.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='fourth_docstring_function')

        assert len(func_obj.lines) == 6
        assert func_obj.docstring == '3 line docstring'
        assert func_obj.returns[0].value == 'fourth_docstring_function_return'

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'fourth_docstring_function'
        assert p_d['name'] == 'docstrings.py'
        assert p_fd['name'] == 'docstrings.py'

    def test_func_init__docstrings__fifth_docstring_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('docstrings.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='fifth_docstring_function')

        assert len(func_obj.lines) == 9
        assert func_obj.docstring == 'indented 3 line docstring'
        assert func_obj.returns[0].value == '\n        fifth_docstring_function_return\n    '

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'fifth_docstring_function'
        assert p_d['name'] == 'docstrings.py'
        assert p_fd['name'] == 'docstrings.py'

    def test_func_init__docstrings__eighth_docstring_function(self):
        from parsefilelib.models.base_lines_obj import BaseLinesObj

        test_file_path = self.get_test_file_path('docstrings.py')
        func_obj = BaseLinesObj(file_path=test_file_path,
                                def_name='eighth_docstring_function')

        assert len(func_obj.lines) == 10
        assert func_obj.docstring == 'docstring that is put all the way to the left'
        assert func_obj.returns[0].value == '\n\n        eighth_docstring_function_return\n\n    '

        d = func_obj.to_dict()
        p_d = func_obj.parent_obj.to_dict()
        p_fd = func_obj.parent_file.to_dict()

        assert d['name'] == 'eighth_docstring_function'
        assert p_d['name'] == 'docstrings.py'
        assert p_fd['name'] == 'docstrings.py'
