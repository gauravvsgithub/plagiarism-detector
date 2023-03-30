import pandas as pd
import ast
import computation as c
submissions = c.submissions
scores = dict()

dp = dict()


def compute_scores():
    global scores
    if len(submissions) <= 1:
        return "Nothing to compare!"

    for i in range(len(submissions)):
        code1, mis1 = submissions[i][1], submissions[i][0]
        for j in range(len(submissions)):
            code2, mis2 = submissions[j][1], submissions[j][0]
            if mis1 not in ast_same_lang_scores:
                ast_same_lang_scores[mis1] = 0
            if mis2 not in scores:
                scores[mis2] = 0
            if mis1 != mis2:
                curr_score = lcs(code1, code2, len(code1), len(code2))
                scores[mis1] = max(scores[mis1], curr_score)
                scores[mis2] = max(scores[mis2], curr_score)

    return "Done!"

def compare_ast():
    pass

def ast_same_lang(code1, code2):
    tree1 = ast.parse(code1)
    tree2 = ast.parse(code2)

    if compare_ast(tree1, tree2):
        print("The two ASTs are similar.")
    else:
        print("The two ASTs are not similar.")

def ast_same_lang_main():
    global ast_same_lang_scores
    if len(submissions) <= 1:
        return "Nothing to compare!"
    
    # copy the code from compute scores
    for i in range(len(submissions)):
        code1, mis1 = submissions[i][1], submissions[i][0]
        for j in range(len(submissions)):
            code2, mis2 = submissions[j][1], submissions[j][0]
            if mis1 not in scores:
                scores[mis1] = 0
            if mis2 not in scores:
                scores[mis2] = 0
            if mis1 != mis2:
                curr_score = lcs(code1, code2, len(code1), len(code2))
                scores[mis1] = max(scores[mis1], curr_score)
                scores[mis2] = max(scores[mis2], curr_score)

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
