# HW12

import statistics as st # 계산 모듈
from matplotlib import pyplot as plt # 그래프 모듈
import sympy as sp # 미분적분 모듈
from sympy.abc import x, y
import numpy as np
import pandas as pd

'''
8.1
'''
# 공분산 행렬
S = np.array([
    [5,2],
    [2,2]])
v, w = np.linalg.eig(S)
v # 고유값
'''array([6., 1.])'''
w # 고유벡터
'''
array([[ 0.89442719, -0.4472136 ],
       [ 0.4472136 ,  0.89442719]])
'''

'''
8.2
'''
S2 = np.array([
    [1,-2,0],
    [-2,5,0],
    [0,0,2]])
v2, w2 = np.linalg.eig(S2)
v2 # 고유값
''' array([0.17157288, 5.82842712, 2.        ])'''
w2 # 고유벡터
'''
array([[-0.92387953,  0.38268343,  0.        ],
       [-0.38268343, -0.92387953,  0.        ],
       [ 0.        ,  0.        ,  1.        ]])
'''
# covariance matrix > correlation matrix 함수
def cor_from_cov(covariance):
    v = np.sqrt(np.diag(covariance))
    outer_v = np.outer(v, v)
    correlation = covariance / outer_v
    correlation[covariance == 0] = 0
    return correlation
p2 = cor_from_cov(S2)
'''
array([[ 1.        , -0.89442719,  0.        ],
       [-0.89442719,  1.        ,  0.        ],
       [ 0.        ,  0.        ,  1.        ]])
'''
p2_v2, p2_w2 = np.linalg.eig(p2)
p2_v2 # 고유값
'''
array([1.89442719, 0.10557281, 1.        ])'''
p2_w2 # 고유벡터
'''
array([[ 0.70710678,  0.70710678,  0.        ],
       [-0.70710678,  0.70710678,  0.        ],
       [ 0.        ,  0.        ,  1.        ]])
'''

'''
8.7
'''
x_bar7 = np.array([39.88,45.08,48.11,49.95])
R7 = np.array([[1,0.7501,0.6329,0.6363],
              [0.7501,1,0.6925,0.7386],
              [0.6329,0.6925,1,0.6625],
              [0.6363,0.7386,0.6625,1]])
v7, w7 = np.linalg.eig(R7)
v7 # 고유값
'''array([3.05841135, 0.2174839 , 0.38232615, 0.3417786 ])'''
w7 # 고유벡터
'''
array([[ 0.49352096,  0.4400815 , -0.71316604, -0.23272202],
       [ 0.5219499 , -0.81890602, -0.19088483,  0.14326277],
       [ 0.48718493,  0.06119812,  0.58542192, -0.64512542],
       [ 0.49664495,  0.36328501,  0.33501995,  0.71353306]])
'''
p7 = cor_from_cov(R7)
p7_v2, p7_w2 = np.linalg.eig(p7)
p7_v2 # 고유값
'''array([3.05841135, 0.2174839 , 0.38232615, 0.3417786 ])'''
p7_w2 # 고유벡터
'''
array([[ 0.49352096,  0.4400815 , -0.71316604, -0.23272202],
       [ 0.5219499 , -0.81890602, -0.19088483,  0.14326277],
       [ 0.48718493,  0.06119812,  0.58542192, -0.64512542],
       [ 0.49664495,  0.36328501,  0.33501995,  0.71353306]])
'''

'''
8.10
'''
stock_price = pd.read_csv('stock_price.csv')
stock_price.info()
'''
RangeIndex: 103 entries, 0 to 102
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   jpmorgan    103 non-null    float64
 1   citibank    103 non-null    float64
 2   wellsfargo  103 non-null    float64
 3   shell       103 non-null    float64
 4   exxon       103 non-null    float64
 '''
stock_price = np.array(stock_price)