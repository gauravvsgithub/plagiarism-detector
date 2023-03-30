# This code ignores variable names and function names and captures the structure of the codes
import ast

def compare_ast(node1, node2):
    """Compares two AST nodes recursively, ignoring variable and function names."""
    if type(node1) != type(node2):
        return False
    if isinstance(node1, ast.AST):
        for field, value1 in ast.iter_fields(node1):
            value2 = getattr(node2, field, None)
            if not compare_ast(value1, value2):
                return False
        return True
    elif isinstance(node1, list):
        if len(node1) != len(node2):
            return False
        return all(compare_ast(x, y) for x, y in zip(node1, node2))
    else:
        if isinstance(node1, ast.Name):
            return isinstance(node2, ast.Name) and node1.id == node2.id
        elif isinstance(node1, ast.Str):
            return isinstance(node2, ast.Str) and node1.s == node2.s
        elif isinstance(node1, ast.Num):
            return isinstance(node2, ast.Num) and node1.n == node2.n
        elif isinstance(node1, ast.FunctionDef):
            if not isinstance(node2, ast.FunctionDef) or len(node1.args.args) != len(node2.args.args):
                return False
            return compare_ast(node1.body, node2.body)
        else:
            return type(node1) == type(node2)

# Example usage
code1 = """
def add(a, b):
    # d stores result of addition
    d = a+b
    return d
"""

code2 = """
def add(a, b):
    c = a+b
    return c
"""

tree1 = ast.parse(code1)
tree2 = ast.parse(code2)

if compare_ast(tree1, tree2):
    print("The two ASTs are similar.")
else:
    print("The two ASTs are not similar.")
