# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:57:03 2020

@author: mohammads6
"""

#https://scikit-learn.org/stable/datasets/index.html

from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)
boston = load_boston()
boston.feature_names
print(boston.DESCR)
X.shape
y.shape

from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()
california.keys()
california.data
california.target
print(california.DESCR)
def(fetch_california_housing) 