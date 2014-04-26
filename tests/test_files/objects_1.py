import ast
import os
from parsefilelib.models.file_obj import FileObj

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

    def bar3(self):
        a = {
    'a': 10
        }
        return a
