import ast
import astor
import esprima
import escodegen
import Levenshtein

# python_code = '''
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# '''

python_code = '''
def helloWorld():
    print("hello world")
    return "This is it"
'''

js_code = '''
function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n-1);
  }
}
'''

def get_ast(code):
    try:
        ast_tree = ast.parse(code)
    except:
        ast_tree = None
    return ast_tree

def get_normalized_ast(code):
    ast_tree = get_ast(code)
    if ast_tree is None:
        return None
    normalized_ast = astor.to_source(ast_tree)
    return normalized_ast

def get_js_ast(code):
    try:
        js_ast = esprima.parseScript(code)
    except:
        js_ast = None
    return js_ast

def get_normalized_js_ast(code):
    js_ast = get_js_ast(code)
    if js_ast is None:
        return None
    normalized_js_ast = escodegen.generate(js_ast)
    return normalized_js_ast

def compare_ast_trees(ast1, ast2):
    if ast1 is None or ast2 is None:
        return False
    distance = Levenshtein.distance(ast1, ast2)
    similarity = 1 - distance/max(len(ast1), len(ast2))
    return similarity >= 0.7

python_normalized_ast = get_normalized_ast(python_code)
js_normalized_ast = get_normalized_js_ast(js_code)

if compare_ast_trees(python_normalized_ast, js_normalized_ast):
    print("Python and JavaScript codes are similar")
else:
    print("Python and JavaScript codes are not similar")
