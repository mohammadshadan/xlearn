# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 00:10:22 2020

@author: mohammads6
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({'Date1': {0: '2016-04-07', 1: '2017-02-01'},
 'Date2': {0: '2017-02-01', 1: '2017-03-05'},
 'Months': {0: 11, 1: 1}})

df.Date1 = pd.to_datetime(df.Date1)
#df.Date1 = df.Date1.dt.strfti
df.Date2 = pd.to_datetime(df.Date2)

# What is np.timedelta64(1,"M"/)
((df.Date2-df.Date1)/np.timedelta64(1,"M")).astype(int)
((df.Date2-df.Date1)/np.timedelta64(1,"D")).astype(int)

from operator import attrgetter
(
    df['Date2'].dt.to_period('M') -
    df['Date1'].dt.to_period('M')).apply(attrgetter('n'))