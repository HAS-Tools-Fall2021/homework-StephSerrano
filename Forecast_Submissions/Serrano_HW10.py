# %%
import os
import matplotlib.pyplot as plt
import matplotlib as mpl 
from matplotlib.dates import DateFormatter
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx
import dataretrieval.nwis as nwis
import json
import urllib.request as req
import urllib
import datetime

#Streamflow Data
#%%
filename = 'streamflow_week10.txt'
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

#Precipitation Data from Mesowest KSEZ (Sedona Airport)
#--------------------------------------------------
# %%
mytoken = '414de9ef1e5148eaad57f338647801c4' # Insert your token here
base_url = "http://api.mesowest.net/v2/stations/timeseries"
# Specific arguments for the data that we want
args = {
    'start': '201810010000',
    'end': '202010300000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum_one_hour',
    'stids': 'ksez',
    'units': 'precip|mm',
    'token': mytoken}

#%%
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# request data
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

#dictionary
responseDict.keys()
responseDict['UNITS']
responseDict['QC_SUMMARY']
responseDict['STATION']
responseDict['SUMMARY']
responseDict['STATION'][0].keys()
responseDict['STATION'][0]['PERIOD_OF_RECORD']
responseDict['STATION'][0]['OBSERVATIONS'].keys()

# Data format
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_one_hour_set_1']

#%%
#Pandas Dataframe
PrecipData = pd.DataFrame({'ACCUMULATION': precip}, index=pd.to_datetime(dateTime))

# Convert to daily data using resample
data_daily = PrecipData.resample('D').mean()

#elements to plot
#%%
datai2 = PrecipData.copy()
datai2.head()
PrecipData.head()
plot_PrecipData= data.iloc[0:365]
#%%
fig, ax = plt.subplots()
ax.plot(datai2['ACCUMULATION'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

#Forecast Predictions: 120 CFS, 110 CFS