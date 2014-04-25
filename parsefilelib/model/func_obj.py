from parsefilelib.model.base_lines_obj import BaseLineObj

class FuncObj(BaseLineObj):
    """
    An object the encapsulates all details of a Function

    Inherits from the BaseLineObj class
    """

    def __init__(self, file_obj, name, lines=None):
        """
        init method for the FileObj class
        """
        super(FuncObj, self).__init__(file_obj, name, lines=lines)
