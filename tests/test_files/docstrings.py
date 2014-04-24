
def first_docstring_function():
    """ Single line docstring """
    return 'first_docstring_function_return'

def second_docstring_function():
    """ 2 line docstring
    """
    return "second_docstring_function_return"

def third_docstring_function():
    """
    2 line docstring part 2 """
    return """third_docstring_function_return"""

def fourth_docstring_function():
    """
    3 line docstring
    """
    return '''fourth_docstring_function_return'''

def fifth_docstring_function():
    """
        indented 3 line docstring
    """
    a = 10
    return """
        fifth_docstring_function_return
    """

def sixth_docstring_function():
    '''
    single quoted docstring
    '''
    b = 20
    c = 30
    return '''
        sixth_docstring_function_return
    '''

def seventh_docstring_function():
    """
    docstring with def in it
    """
    c = 30
    return '''

        sixth_docstring_function_return

    '''
