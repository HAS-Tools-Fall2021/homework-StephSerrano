#%%
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
from netCDF4 import Dataset
from sklearn.linear_model import LinearRegression

# Embedded USGS streamflow
flow_url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb" \
              "&site_no=09506000&referred_module=sw" \
              "&period=&begin_date=1989-01-01&end_date=2021-12-4"
flow_data = pd.read_table(flow_url, sep='\t', skiprows=30,
                          names=['agency_cd', 'site_no', 'datetime', 'flow',
                                 'code'], parse_dates=['datetime'],
                          index_col=['datetime'])
flow_data['month'] = pd.DatetimeIndex(flow_data.index).month
flow_data['day'] = pd.DatetimeIndex(flow_data.index).day
flow_data['year'] = pd.DatetimeIndex(flow_data.index).year

# December Flow function
def Monthly_ObservedFlow(startyear, endyear, month, firstday, lastday):
       '''Variables:
       flow_data: USGS Streamgage 09506000 daily streamflow data values
       startyear: First year being viewed intimeseries
       endyear: Final year being viewed in timeseries
       month: Month being viewed in timeseries
       firstday: First day of month
       lastday: Last day of month'''

       fig, ax = plt.subplots()
       for x in range(startyear, endyear):
              plot = flow_data[(flow_data.index.year == x) &
                        (flow_data.index.month == month) &
                        (flow_data.index.day >= firstday) &
                        (flow_data.index.day <= lastday)]
       ax.plot(plot.index.day, plot['flow'],
                        label=x)
       ax.set(title='Observed Flow',yscale='log', 
              ylabel='Log Flow (cfs)')
       plt.show()

       return fig

Monthly_ObservedFlow(2015, 2021, 12, 1, 31)

fig = plt.figure()
fig.savefig('DecFlow.png')

# Week 1 Linear Regression
flow_weekly = flow_data
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)
train = flow_weekly[2:800][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[800:][['flow', 'flow_tm1', 'flow_tm2']]
model = LinearRegression()
x = train['flow_tm1'].values.reshape(-1, 1)
y = train['flow'].values
model.fit(x, y)
r_sq = model.score(x, y)

# Week 2 Linear Regression
flow_weekly2 = flow_data
flow_weekly2['flow_tm1'] = flow_weekly2['flow'].shift(1)
flow_weekly2['flow_tm2'] = flow_weekly2['flow'].shift(2)
train = flow_weekly2[2:800][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly2[1000:][['flow', 'flow_tm1', 'flow_tm2']]
model2 = LinearRegression()
x = train['flow_tm2'].values.reshape(-1, 1)
y = train['flow'].values
model2.fit(x, y)
r_sq = model.score(x, y)

print('Week 1 Prediction:', np.round(model.intercept_, 2)+100)
print('Week 2 Prediction:', np.round(model2.intercept_, 2)+100)

# %%
