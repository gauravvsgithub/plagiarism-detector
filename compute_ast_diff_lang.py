import pandas as pd

import astor
import esprima
import javalang
import clang.cindex as cindex

import computation as c
submissions = c.submissions
scores = dict()

dp = dict()

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

def compute_scores():
    global scores
    if len(submissions) <= 1:
        return "Nothing to compare!"
    
    # copy the code from compute scores
    for i in range(len(submissions)):
        code1, mis1 = submissions[i][1], submissions[i][0]
        for j in range(len(submissions)):
            code2, mis2 = submissions[j][1], submissions[j][0]
            if mis1 not in scores:
                scores[mis1] = -1
            if mis2 not in scores:
                scores[mis2] = -1
            if mis1 != mis2:
                tree1 = ast.parse(code1)
                tree2 = ast.parse(code2)
                curr_score = compare_ast(tree1, tree2)
                if curr_score:
                    scores[mis1] = mis2
                    scores[mis2] = mis1

    return "Done!"

    
    

def getDataFrame():
    global scores
    data = dict()
    data['MIS No'] = []
    data['Plagiarism Score'] = []
    for key, val in scores.items():
        data['MIS No'].append(key)
        data['Plagiarism Score'].append(val)
    df = pd.DataFrame.from_dict(data)
    return df
