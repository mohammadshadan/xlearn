# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:57:07 2023

@author: mohammads6
"""

my_dict = {'A': 300, 'B': 150, 'C': 500, 'D': 850, 'E': 400}

my_dict.values().count


# import pandas module
import pandas as pd
 
# create dataframe with 3 columns
data = pd.DataFrame({
    "id": [7058, 7059, 7072, 7054],
    "name": ['sravan', 'jyothika', 'harsha', 'ramya'],
    "subjects": ['java', 'python', 'html/php', 'php/js']
}
)


data

data.iloc[[2]]
data.loc[[2]]
data.iloc[[0],:]
data.iloc[0].to_frame()
 
# get first row using row position
print(data.iloc[0])
 
print("---------------")
 
# get first row using slice operator
print(data.iloc[:1])