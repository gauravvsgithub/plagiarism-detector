import pandas as pd
submissions = []
scores = dict()

dp = dict()

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0

    elif X[m - 1] == Y[n - 1]:
        if (m-1, n-1) not in dp:
            dp[(m-1, n-1)] = lcs(X, Y, m - 1, n - 1)
        
        return 1 + dp[(m-1, n-1)]
    else:
        if (m-1, n) not in dp:
            dp[(m-1, n)] = lcs(X, Y, m-1, n)
        if (m, n-1) not in dp:
            dp[(m, n-1)] = lcs(X, Y, m, n-1)
        return max(dp[(m-1, n)], dp[(m, n-1)])


def compute_scores():
    global scores
    if len(submissions) <= 1:
        return "Nothing to compare!"

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
