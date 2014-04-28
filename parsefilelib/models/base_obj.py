
class BaseObj(object):
    """
    An object that encapsulates all details of an object for the purposes of
        this project
    """

    def __init__(self, ast_node, parent_obj=None,
                    parent_file=None, file_lines=None, line_number=0, indent=0,
                    file_path=None, line_index_end=0, obj_type=None):
        from parsefilelib.models.base_lines_obj import node_type
        """
        init method for the BaseObj
        """
        # Set ast_node
        self.ast_node = ast_node

        if not self.ast_node:
            return

        self.line_index_start = self.ast_node.lineno - 1
        self.line_index_end = line_index_end
        self.parent_obj = parent_obj
        if obj_type:
            self.obj_type = obj_type
        else:
            self.obj_type = node_type(self.ast_node)

        if self.obj_type == 'import':
            self.imps = []
            if hasattr(self.ast_node, 'module'):
                self.module = self.ast_node.module
            if hasattr(self.ast_node, 'level'):
                self.level = self.ast_node.level
            for n in self.ast_node.names:
                self.imps.append({'name': n.name, 'asname': n.asname})
        elif self.obj_type == 'decorator':
            if hasattr(self.ast_node, 'func'):
                self.name = self.ast_node.func.id
                self.args = self.ast_node.args
                self.keywords = self.ast_node.keywords
                self.starargs = self.ast_node.starargs
                self.kwargs = self.ast_node.kwargs
            else:
                self.name = self.ast_node.id
        else:
            if hasattr(self.ast_node.value, 's'):
                self.value = self.ast_node.value.s
            elif hasattr(self.ast_node.value, 'n'):
                self.value = self.ast_node.value.n
            elif hasattr(self.ast_node.value, 'id'):
                self.value = self.ast_node.value.id

            if self.obj_type == 'assign':
                self.targets = []
                for t in self.ast_node.targets:
                    if hasattr(t, 's'):
                        self.target = t.s
                    elif hasattr(t, 'n'):
                        self.target = t.n
                    elif hasattr(t, 'id'):
                        self.target = t.id
