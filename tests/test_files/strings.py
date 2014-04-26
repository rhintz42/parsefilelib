import ast
import os
from parsefilelib.models.file_obj import FileObj
from parsefilelib.models.base_lines_obj import BaseLinesObj, node_type,\
                                                fetch_ast_node as fetch_node

class Foo():
    """
def hello():
    cool

def nice
    """

    def bar(self):
        """
class Cool():
        """
        return 'bar function'

    def bar2(self):
        return """
    def bar2(self)
    """
