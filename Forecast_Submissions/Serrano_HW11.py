#%%
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset

#%%
filepath = os.path.join('../data', 'streamflow_week11.txt')
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek
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

#--------
# Reanlysis Daily Average - Precipitation Rate
# Class example w/ slightly different dates and coordinates
# Mostly just testing if I can get the initial code to work
# Especially since I have been having trouble w/ directories
# %%
# Net CDF file historical time series
# Data Range: Jan 1, 2010 - Sept. 30, 2021
os.getcwd()

#%%
data_path = os.path.join('../data', 'Reanalysis_PrecipAZ.nc')

#%%
# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# look at it
dataset


# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata
# And we can grab out any part of it like this:
metadata['dataset_title']

# we can also look at other  attributes like this
dataset.values
dataset.dims
dataset.coords

# Focusing on just the precip values
precip = dataset['prate']
precip

# Now to grab out data first lets look at spatail coordinates:
dataset['prate']['lat'].values.shape
# The first 4 lat values
dataset['prate']['lat'].values
dataset['prate']['lon'].values

# Now looking at the time;
dataset["prate"]["time"].values
dataset["prate"]["time"].values.shape


# Now lets take a slice: Grabbing data for just one point
lat = dataset["prate"]["lat"].values[0]
lon = dataset["prate"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset["prate"].sel(lat=lat,lon=lon)
one_point.shape


# use x-array to plot timeseries
one_point.plot.line()

# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
one_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="green",
                    markeredgecolor="green")
ax.set(title="Time Series For a Single Lat / Lon Location")

#Convert to dataframe
one_point_df = one_point.to_dataframe()

# Strip out just the values
precip_val = one_point.values

# %%
# Making a spatial map of one point in time
start_date = "2018-11-08"
end_date = "2018-11-08"

timeslice = dataset["prate"].sel(
    time=slice(start_date, end_date))

timeslice.plot()

# ----------------------------
# Reanalysis Daily Average - Air Temperature
# Jan. 1st, 2010 - Nov. 5th, 2021
#%%
data_pathAT = os.path.join('../data', 'Reanalysis_AirTempVWS.nc')

#%%
# Read in the dataset as an x-array
datasetAT = xr.open_dataset(data_pathAT)
# look at it
datasetAT

#%%
# We can inspect the metadata of the file like this:
metadata = datasetAT.attrs
metadata

#%%
# This gives info about the file
# The data variable is titled 'air':
dataset['air']

#%%
# Focusing on just the airtemp values
AirTemp = dataset['air']
AirTemp

#%%
# Now to grab out data first lets look at spatail coordinates:
dataset['air']['lat'].values.shape
# The first 4 lat values
dataset['air']['lat'].values
dataset['air']['lon'].values

# Now looking at the time;
dataset["air"]["time"].values
dataset["air"]["time"].values.shape


# Grabbing data for just one point (slice)
lat = dataset["air"]["lat"].values[0]
lon = dataset["air"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset["air"].sel(lat=lat,lon=lon)
one_point.shape


# use x-array to plot timeseries
one_point.plot.line()

# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
one_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="green",
                    markeredgecolor="green")
ax.set(title="Time Series For a Single Lat / Lon Location")

#Convert to dataframe
one_point_df = one_point.to_dataframe()

# Strip out just the values
air_val = one_point.values

# %%
# Making a spatial map of one point in time
# This was just a negative trending line..
start_date = "2018-11-08"
end_date = "2018-11-08"

timeslice = dataset["air"].sel(
    time=slice(start_date, end_date))

timeslice.plot()
# %%
