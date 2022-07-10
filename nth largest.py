# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:34:49 2020

@author: mohammads6
"""
import pandas as pd
Employee={'EMPNO':(111,112,114,115,223,226,228,300,333,345,356,320),'Salary':(4000,6000,2000,8000,2000,1000,3000,500,700,300,200,700),'EMPCODE':('MGF','MGR','MGR','MGR','CLERK','CLERK','CLERK','PEON','PEON','PEON','PEON','PEON')}

Employee          

emp_df=pd.DataFrame(Employee)

emp_df

emp_df.groupby("EMPCODE").sort_values("Salary")

output = emp_df.sort_values(["EMPCODE", "Salary"], ascending=[True, False])
n=1 # numbering starts from 0
output.groupby(["EMPCODE"]).nth(n).reset_index()
