# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)


# %%
# Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

#%%
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

#%%
#Min, Max, Std., etc. for all months
Data1 = data.groupby("month")["flow"]

Data1.describe()

#%%
#Flow Scatterplot for the month of October
oct_data = data[data['month']==10] 
fig, ax = plt.subplots()
ax.scatter(oct_data['day'], oct_data['flow'], alpha=0.2,
            s=0.02*oct_data['flow'], c=oct_data['year'], cmap='magma')
ax.set(yscale='log')
ax.set_xlabel('Day of the month')
ax.set_ylabel('Flow')
plt.show()
fig.set_size_inches(5,3)
fig.savefig("Scatterplot_Oct_Flow.png")

# %%
#Observed Avg. Weekly Flow for Oct. 1, 2017 to Nov. 15th, 2017.
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], label='flow')
ax.set(title="Observed Flow Fall 2017 Trend", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2017, 10, 1), datetime.date(2017, 11, 15)])
ax.legend()
plt.show()
fig.set_size_inches(5,3)
fig.savefig("Observed_Fall_2017_Flow.png")

#%%
#October flows for 2010 to 2018
mypal = sns.color_palette('plasma', 12)
mypal
colpick = 0
fig, ax = plt.subplots()
for i in range(2010, 2019):
        plot_data=data[(data['year']==i) & (data['month']==10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                color=mypal[colpick], label=i)
        ax.set(yscale='log')
        ax.legend()
        colpick = colpick+1

fig.set_size_inches(5,3)
fig.savefig("Oct_2010-2018_Flow.png")
# %%
