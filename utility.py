import pandas as pd
import numpy as np
import csv

# x must be a numpy matrix
def normalize_matrix_by_col(x, v):
    _x = x.copy()
    for i in range(len(_x)):
        count = 0
        for j in range(len(_x[i])):
            if (_x[i][j] != v):
                count += 1
        _x[i] = len(_x[i]) * _x[i] / count
    return _x
# x must be a numpy matrix
def normalize_matrix_by_row(x, v):
    _x = x.copy()
    
    _x = _x.transpose()
    _x = normalize_matrix_by_col(_x, v)
    _x = _x.transpose()
    return _x

def load_user_business_matrix():
    path = "user_business_matrix.csv"
    df = pd.read_csv(path)
    users = df.values[:, 1]
    business = np.array(list(map(int, list(df.columns)[2:])))
    matrix = df.values[0:, 2:]
    return (users, business, matrix)

    
