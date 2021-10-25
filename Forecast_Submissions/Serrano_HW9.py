#%%
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

#%%
filename = 'streamflow_week9.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

#%%
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime'])

#%%
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

#This is p much stolen from Week8 TimeSeries Examples
# %%
datai = data.copy()
datai = datai.set_index('datetime')
datai.head()
data.head()

#%%
fig, ax = plt.subplots()
ax.plot(datai['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

# %%
data = data.copy()
print(data.dtypes)
data['datetime'] = pd.to_datetime(data['datetime'])
print(data.dtypes)

# %%
#Plot of Median, Min, Max, and 2017 flow
oct_flow = datai[datai.index.month == 10]
datai['day'] = datai.index.day
oct_median = datai.groupby(datai.index.day).median()
oct_median = datai.groupby('day').median()
oct_max = datai.groupby('day').max()
oct_min = datai.groupby('day').min()

fig, ax = plt.subplots()
ax.plot(oct_median['flow'], color='grey',
        linestyle='dashed', label='Median')
ax.fill_between(oct_max.index, oct_min['flow'], oct_max['flow'], color = 'blue', alpha=0.1)
ax.plot(oct_min['flow'], color='blue', linestyle='dashed', label='Min')
ax.plot(oct_max['flow'], color='blue', linestyle='dashed', label='Max')
ax.plot(oct_flow["2017"].day, oct_flow["2017"].flow, color='black', label='2017 flow')
ax.set(title="Observed Oct. Flow", xlabel="Date",
       ylabel="Daily Avg Flow [cfs]",
       yscale='log')
ax.legend()

#---------------------------
# attempt at loading in the URL precip data... did not work
# %%
url = "https://rain.flagstaffaz.gov/JEFDAQFLASK/tabular_data/?sensorPair=3400:3400&dur=8640000&startDate=1633046400000&endDate=1634947200000"

PrecipData = pd.read_table(url, skiprows=6, names=['Data','Time','Precipitation'],)

# %%
plot_PrecipData  = PrecipData.iloc[0:24]

fig, ax = plt.subplots()
ax.plot(PrecipData['datetime'], plot_PrecipData['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

fig, ax = plt.subplots()
ax.plot(PrecipData['datetime'], PrecipData['flow'])
ax.set(title="Observed Daily Precip", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
# %%
