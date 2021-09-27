# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week5.txt'

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :)
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

# Entering any of these 3 gives the amount of rows and columns (11956 rows x 8 columns)
data

data.info 

data.shape

# Same thing but the two are separated
len(data)
len(data.columns)

#ANOTHER way to do it
row, col = data.shape
print(row)
print(col)

#This is the number of elements
data.size

# This is the data types for each column (also lists the names of each)
data.dtypes

# Q2: Provide summary of the flow column
data[["flow"]].describe()

# Q3: Provide summary of the flow column on a monthly basis
test1 = data.groupby("month")["flow"]

test1.describe()

# Q4: 5 Highest and Lowest Flow Values
data.sort_values(by="flow")

# Q5: Min and Max of each month (maybe doing this wrong but the code for Q3 provided that)
test1 = data.groupby("month")["flow"]

test1.describe()

# Q6: Which flows are within 10% of my Week 1 Forecast Value?
#here are a bunch of failed tests i tried
data.loc[data['flow']] >= 216

t1 = ['flow']
t2 = data('flow')

data.loc[data['flow'] <= 264, '<=264'] = 'True'
data.loc[data['flow'] >= 216, '>=216'] = 'True'

data


data.loc[(data['flow'] >= 216) and (data['flow'] <= 264)].values


print(data.loc[(data['flow'] >= 216)] and data.loc[(data['flow'] <= 264)])

print(data.loc[(data['flow'] <= 264) and data.loc[(data['flow'] >= 216)])

#I couldn't exactly figure it out but there are a LOT of values that are within 10% of 240 so I just wrote down what values were actually 240 for now.
print(data.loc[(data['flow'] == 240)])