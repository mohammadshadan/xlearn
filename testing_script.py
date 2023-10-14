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

df["Start_Date"].dt.month_name()

df["Start_Date"].dt.year

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

import numpy as np
import pandas as pd
df = pd.read_csv("D:/Drive/projects/Other Projects/Digital Twin/Sprints/Sprint 5/organised_final_train_v1.csv")
df =df.dropna(axis=0, subset=["cc_smooth"])
df_p = df.groupby('cycle_index').agg(
    soh_mean =('soh_pred_smooth', 'mean'), 
    soh_std =('soh_pred_smooth', 'std'),
    temperature_mean=('temperature', 'mean'),
    temperature_std=('temperature', 'std'),
    cc_mean=('cc_smooth', 'mean'),
    cc_std=('cc_smooth', 'std'),
    voltage_mean=('voltage_smooth', 'mean'),
    voltage_std=('voltage_smooth', np.nanstd),
    seg_33_34_mean=('seg_3.2_3.3_smooth', 'std'),
    battery_count = ('soh_pred_smooth', 'count')
    ).reset_index()

df_p = df.groupby('cycle_index').agg({
    'soh_pred_smooth':['mean', 'std'],
    'voltage': ['mean','std','count']})


df_p = df.groupby('cycle_index').agg(

def grouped_df:
    for col in gropued_df.columns:
        
df_p = df.groupby('cycle_index').lambda()

df_p
df_p = df_population.fillna(0)

df_p["soh_minstd"] = df_p["soh_mean"] - df_p["soh_std"]
df_p["soh_maxstd"] = df_p["soh_mean"] + df_p["soh_std"]


df_p["cc_minstd"] = df_p["cc_mean"] - df_p["cc_std"]
df_p["cc_maxstd"] = df_p["cc_mean"] + df_p["cc_std"]

df_p["temperature_minstd"] = df_p["temperature_mean"] - df_p["temperature_std"]
df_p["temperature_maxstd"] = df_p["temperature_mean"] + df_p["temperature_std"]

df_p["voltage_minstd"] = df_p["voltage_mean"] - df_p["voltage_std"]
df_p["voltage_maxstd"] = df_p["voltage_mean"] + df_p["voltage_std"]

arragned_columns = ["cycle_index", 
                    "soh_mean", "soh_minstd", "soh_maxstd",
                    "cc_mean", "cc_minstd", "cc_maxstd",
                    "voltage_mean", "voltage_minstd", "voltage_maxstd",
                    "temperature_mean", "temperature_minstd", "temperature_maxstd",
                    "battery_count"]
df_p = df_p[arragned_columns]


df_population
import statistics
set1 =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]


# How to find the number of days in the month

from calendar import monthrange
year = 2022 
month = 2   #choose a month number from 1-12 
num_of_days = monthrange(2022, 3)[1]
print(num_of_days)
help(monthrange)


import pandas as pd

month_number = [1,2,3,4,5,6,7,8,9,10]
pd.to_datetime(month_number, format="%m")


strftime

import pandas as pd

df = pd.DataFrame({'Name': ['Mark', 'Laura', 'Adam', 'Roger', 'Anna'],
                   'City': ['Lisbon', 'Montreal', 'Lisbon', 'Berlin', 'Glasgow'],
                   'Car': ['Tesla', 'Audi', 'Porsche', 'Ford', 'Honda']})

import numpy as np
df = pd.DataFrame({'col11': np.arange(0,40,2),
                   'col22': np.arange(0,100,5),
                   'col33': np.arange(0,120,6),
                   'cycle_number': np.arange(0,20,1)})

df

dff = df.head(1).iloc[-1]

dff.dropna().iloc[1:-1]

pd.DataFrame(df.head(1).iloc[[-1]])

# =============================================================================
# Quadratic Data
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

def generate_quadratic_data(num_points, a, b, c, noise):
    x = np.linspace(-10, 10, num_points)
    y = a*x**2 + b*x + c + np.random.normal(scale=noise, size=num_points)
    return x, y

# Generate quadratic data with a=1, b=2, c=3 and noise=2
x, y = generate_quadratic_data(100, 1, 2, 3, 2)
plt.plot(x,y)
df = pd.DataFrame({"x":x,
                   "y":y,
                   "cycle_number":np.arange(len(x))})

df.plot("cycle_number", "y" )
df.plot("y", "x")

dff = gaussian_filter__(df.head(2),"x", col2, b=4)
dff

dff_ = pd.DataFrame([dff.smoothed.iloc[-1]]) 


# Print the first 5 points
print(list(zip(x[:5], y[:5])))



col2= "cycle_number"
def gaussian_filter__(data,col1,col2,b=120):
        
    dff = data[[col1,col2]]
    #dff = dff.dropna().iloc[1:-1]
    dff['Time_'] = np.arange(len(dff))
    smoothed_cases = []

    for date in sorted(dff.Time_):
        #print(date)
        dff['gkv'] = np.exp(
            -((dff['Time_'] - date) ** 2) / (2 * (b ** 2))
        )
        # print(np.exp(
        #     -((dff['Time_'] - date) ** 2) / (2 * (6 ** 2))
        # ))
        dff['gkv'] /= dff['gkv'].sum()
        # print(dff['gkv'])
        smoothed_cases.append((dff[col1] * dff['gkv']).sum())
        
    dff['smoothed'] = smoothed_cases
    return dff

dff = gaussian_filter__(df.head(10),"col11", col2, b=4)
dff_ = pd.DataFrame([dff.smoothed.iloc[-1]]) 

dff.reset_index().plot(y=["col11", "smoothed"], x="index")

# When gaussian_filter__ is run the leght of the output reduces by 2
# If there are 

# =============================================================================
# 
# =============================================================================

import numpy as np
from scipy.ndimage import gaussian_filter1d

def gaussian_filter_timeseries(timeseries, sigma):
    """
    Apply Gaussian filtering to a time series.

    Parameters:
    timeseries (numpy.ndarray): 1D array of the time series data.
    sigma (float): Standard deviation of the Gaussian kernel.

    Returns:
    numpy.ndarray: Filtered time series data.
    """
    filtered = gaussian_filter1d(timeseries, sigma=sigma)
    return filtered


import matplotlib.pyplot as plt

# Generate a sample time series
time = np.linspace(0, 10, num=1000)
data = np.sin(time) + np.random.normal(0, 0.1, size=len(time))

# Apply Gaussian filtering with sigma=5
filtered_data = gaussian_filter_timeseries(data, sigma=5)
filtered_data.shape

# Plot the original and filtered data
fig, ax = plt.subplots()
ax.plot(time, data, label='Original')
ax.plot(time, filtered_data, label='Filtered')
ax.legend()
plt.show()


gaussian_filter_timeseries(data[0:10], sigma=5)