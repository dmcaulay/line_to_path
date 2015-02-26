import ast


class MethodFinder(ast.NodeVisitor):
    def __init__(self, line_to_match):
        self.line_to_match = line_to_match
        self.current_class = None
        self.current_function = None
        self.log_name = False
        self.lines = []
        self.function_dict = {}

    def visit_ClassDef(self, node):
        self.log_name = True
        self.current_class = node.name
        self.current_function = None
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.log_name = True
        self.current_function = node.name
        self.generic_visit(node)

    def generic_visit(self, node):
        if self.log_name:
            current_line_num = getattr(node, 'lineno', -1)
            self.lines.append(current_line_num)
            if self.current_function:
                self.function_dict[current_line_num] = ".%s.%s" % (self.current_class, self.current_function)
            else:
                self.function_dict[current_line_num] = ".%s" % (self.current_class)
            self.log_name = False
        super(MethodFinder, self).generic_visit(node)


class PathFinder:
    def __init__(self, file_name, line_num):
        self.file_name = file_name
        self.line_num = line_num

    def get_name(self):
        with open(self.file_name, 'r') as f:
            ast_node = ast.parse(f.read())
        finder = MethodFinder(self.line_num)
        finder.visit(ast_node)
        matched_function = ""
        for line in finder.lines:
            if line > self.line_num:
                break
            matched_function = finder.function_dict.get(line)
        return matched_function
