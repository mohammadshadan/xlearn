"""
Created on Mon Sep 30 14:08:29 2019

@author: mohammads6
"""

# =============================================================================
# Merging (joining) multiple dataframe using pandas
# =============================================================================
# https://stackoverflow.com/questions/23668427/pandas-three-way-joining-multiple-dataframes-on-columns
# https://www.geeksforgeeks.org/reduce-in-python/

import numpy as np
import pandas as pd
from functools import reduce

df1 = pd.DataFrame(np.array([
    ['a', 5, 9],
    ['b', 4, 61],
    ['c', 24, 9]]),
    columns=['name', 'A', 'B']
)
df2 = pd.DataFrame(np.array([
    ['a', 5, 19],
    ['b', 14, 16],
    ['c', 4, 9]]),
    columns=['name', 'C', 'D']
)
df3 = pd.DataFrame(np.array([
    ['a', 15, 49],
    ['b', 4, 36],
    ['c', 14, 9]]),
    columns=['name', 'E', 'F']
)

df1
df2
df3

dfs = [df1, df2, df3]
df_final = reduce(lambda left,right: pd.merge(left,right,on='name'), dfs)

# =============================================================================
# How to create a Pandas Dataframe from Scratch
# =============================================================================

import pandas as pd
df = pd.read_csv("bit.ly/ds-mtcars")


## Create Pandas Data Frame
import pandas as pd
df = pd.DataFrame({'user': ['Bob', 'Jane', 'Alice'], 
                   'income': [40000, 50000, 42000]})
df

# =============================================================================
# Sort a pandas dataframe on one column
# =============================================================================
import pandas as pd
df = pd.read_clipboard()
df["1"].to_list()

month_name = ['August',  'April',  'December',  'February',  'January',
 'July', 'June',  'March',  'May', 'November', 'October', 'September']

month_number = [8,4,12,2,1,7,6,3,5,11,10,9]
months_df = pd.DataFrame({"month_name":month_name,
                          "month_number":month_number})
months_df
#months_df["num_of_days"] = pd.to_datetime(months_df["month_name"], format="%B")
#months_df["num_of_days"] = months_df["num_of_days"].dt.days_in_month
months_df["num_of_days"] = [31, 30, 31, 28, 31, 31, 30, 31, 31, 30, 31, 30]
#months_df["start_alphabet"] = months_df["month_name"].str[0]
months_df = months_df[["month_name","num_of_days", "month_number"]]
months_df

months_df.info()
months_df.sort_values("month_number")
months_df.sort_values("month_number", ascending=True)
months_df.sort_values("month_number", ascending=False)
months_df.sort_values("month_name")["month_name"].str[-1]

x = pd.to_datetime(months_df["month_name"], format="%B")
x.dt.days_in_month
x.dt.daysinmonth

# =============================================================================
# Sort a pandas dataframe on two columns
# =============================================================================
months_df.sort_values(["num_of_days"])
months_df.sort_values(["num_of_days", "month_number"])
# =============================================================================
# How to find the number of days in a month using pandas
# https://stackoverflow.com/questions/28819470/numbers-of-day-in-month
# =============================================================================
import numpy as np
import pandas as pd

x = pd.DataFrame({"col1":[1,2,np.nan,5],
              "col2":[np.nan, np.nan, 4, 7]})
x.columns = ["col1", "col1"]

x.groupby(level=0, axis=1).sum()
x.groupby(level=0, axis=1).count()
x.groupby(level=0, axis=1).mean()


x = pd.DataFrame({"col1":[1,2,np.nan,5],
              "col2":[np.nan, np.nan, 4, 7],
              "col3":[1,2,3,4]})
x.columns = ["col1", "col1", "col1"]

x.groupby(level=0, axis=1).sum()
x.groupby(level=0, axis=1).count()
x.groupby(level=0, axis=1).mean()


# =============================================================================
# pandas str.strip
# =============================================================================
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df[["PPG", "P"]].shift(0)
df["PPG"].values.reshape(-1,1)
df.SALARY.str.replace("[$m]","")

df.SALARY.str.strip("$m")

# =============================================================================
# How to convert string into dates using pandas
# =============================================================================
#How to convert string to datetime format in pandas python?

d1 <- "January 1, 2010"
d2 <- "2015-Mar-07"
d3 <- "06-Jun-2017"
d4 <- c("August 19 (2015)", "July 1 (2015)")
d5 <- "12/30/14" # Dec 30, 2014

d1 = pd.to_datetime("January 1, 2010")
d2 =  pd.to_datetime("2015-Mar-07")
d3 = pd.to_datetime("06-Jun-2017")
pd.to_datetime("August 19 (2015)", format = "%B %d (%Y)")
d4 = pd.to_datetime(pd.Series(["August 19 (2015)", "July 1 (2015)"]),format = "%B %d (%Y)")
d4.dt.date
 pd.to_datetime(["January 1, 2010", "2015-Mar-07"])
d5 <- pd.to_datetime("12/30/14") # Dec 30, 2014

# =============================================================================
# Indices of Group By 
# =============================================================================

import pandas as pd
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})

df_grouped = df.groupby("Animal").apply(lambda x: x.index.tolist())
df_grouped


df.index.str
df.groupby("Animal").apply(lambda x: x.index.tolist()).reset_index()
type(df.columns)
df.columns.map('|'.join)

print(df.index.tolist())

df.index.tolist().map("|".join)
type(df.index)
[1,2,3,4].join("_")

" ".join([1,2,3])

pd.Series(df.index).map('|'.join)

map(" ".join, df.columns)


# =============================================================================
# Extrack Week day name
# ============================================================================= 
df = pd.DataFrame({"Start_Date":['2017-01-01', '2017-01-09', '2017-01-23',
                                 '2017-02-01','2017-12-31']})
df["Start_Date"] = pd.to_datetime(df["Start_Date"])
df["Start_Date"].dt.day_name()



# =============================================================================
# Pandas Explode
# How to turn a pandas cell containing a list into rows for each of those values
# =============================================================================
import pandas as pd
pd.__version__

# https://stackoverflow.com/questions/32468402/how-to-explode-a-list-inside-a-dataframe-cell-into-separate-rows
# https://stackoverflow.com/questions/53218931/how-to-unnest-explode-a-column-in-a-pandas-dataframe
# https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe/50731254#50731254
df = (pd.DataFrame({'name': ['A.J. Price'] * 3, 
                    'opponent': ['76ers', 'blazers', 'bobcats'], 
                    'nearest_neighbors': [['Zach LaVine', 'Jeremy Lin', 'Nate Robinson', 'Isaia']] * 3})
      .set_index(['name', 'opponent']))

df.explode("nearest_neighbors").reset_index()
df.explode("nearest_neighbors").shape


# =============================================================================
# 
# =============================================================================
df = pd.DataFrame({"TIME_STAMP":['2017-10-01 15:23:25', '2017-10-09 00:12:58', '2017-10-23 19:55:03',
                                 '2017-11-06 19:24:31', '2017-11-26 12:25:49', '2017-11-27 18:11:49',
                                 '2017-12-18 08:02:36']})
df["TIME_STAMP"] = pd.to_datetime(df["TIME_STAMP"])

df["MINUTE_SECOND"] = pd.to_datetime(df["TIME_STAMP"].dt.strftime("%M:%S"), format="%M:%S")
df["y"] = [1,2,3,4,5,6,7]

df.plot(x="MINUTE_SECOND", y="y")

# =============================================================================
# if my date format in CSV file is day and month (example, 10-May), 
# how do I change the datatype to date time?
# =============================================================================

start_date_list = ["10-May", "01-Jan", "31-Dec"]
df = pd.DataFrame({"start_date":start_date_list})
df["start_date"] = pd.to_datetime(df["start_date"], format="%d-%b")


d = pd.Series(["10-May"])
pd.to_period(d)
d.dt.strftime(format="%d-%b")


# =============================================================================
# Python Pandas max value in a group as a new column
# https://stackoverflow.com/questions/35640364/python-pandas-max-value-in-a-group-as-a-new-column
# https://stackoverflow.com/questions/27517425/apply-vs-transform-on-a-group-object
# =============================================================================
import numpy as np
import pandas as pd
data = pd.DataFrame({'group' : ['A', 'A', 'A','B','B'],
    'odds' : [85, 75, 30, 60, 65]})

data
data = pd.DataFrame({'group' : ['A', 'B', 'A','B','A'],
    'odds' : [85, 65, 30, 60, 75]})
data

data["max"] = data.groupby("group")["odds"].transform("max")
data.groupby("group")["odds"].transform("min")
data.groupby("group")["odds"].transform("count")
data.groupby("group")["odds"].transform("sum")
data.groupby("group")["odds"].transform(np.mode)


# =============================================================================
# Multiple aggregations of the same column using pandas GroupBy.agg()
# https://stackoverflow.com/questions/12589481/multiple-aggregations-of-the-same-column-using-pandas-groupby-agg
# =============================================================================
import pandas as pd
# Setup
df = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'],
                   'height': [9.1, 6.0, 9.5, 34.0],
                   'weight': [7.9, 7.5, 9.9, 198.0]
})

df.groupby('kind').agg(
    max_height=('height', 'max'), 
    min_height=('height', 'min'),
    min_weight=('weight', 'min')
    ).reset_index()


df.groupby("kind").agg({'height': [('max_height', 'max'), ('min_height', 'min')]})



import statistics
set1 =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]
