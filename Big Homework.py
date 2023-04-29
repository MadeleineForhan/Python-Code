# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sbs
from scipy import stats
##############
#file
file = 'C:/Users/mmfor/Downloads/Python Data Sets/SWdata.csv'
data = pd.read_csv(file, skiprows = 115, skipfooter = 3, usecols=[1,2,3,4,5,6,7])

#rename

new_columns= ['time', 'speed','density','temp','ratio','plasma','symH'] 
data.columns = new_columns         

#####
#bad data
data.speed[data.speed == 99999.9] = np.nan
data.density[data.density == 999.99] = np.nan
data.temp[data.temp > 9999999] = np.nan
data.ratio[data.ratio == 9.999] = np.nan
data.plasma[data.plasma == 999.99] = np.nan

#################
#%%
plt.figure(1)
plt.subplot(6,1,1)
plt.plot(data.time, data.speed, c='red')
plt.xlabel('time')
plt.ylabel('speed')

plt.subplot(6,1,2)
plt.plot(data.time, data.density, c='orange')
plt.xlabel('time')
plt.ylabel('density')

plt.subplot(6,1,3)
plt.plot(data.time, data.temp, c='yellow')
plt.xlabel('time')
plt.ylabel('temp')

plt.subplot(6,1,4)
plt.plot(data.time, data.ratio, c='limegreen')
plt.xlabel('time')
plt.ylabel('Na/Np \nRatio')

plt.subplot(6,1,5)
plt.plot(data.time, data.plasma, c= 'blue')
plt.xlabel('time')
plt.ylabel('Plasma \nBeta')

plt.subplot(6,1,6)
plt.plot(data.time, data.symH, c='purple')
plt.xlabel('time')
plt.ylabel('SymH')

plt.subplots_adjust(hspace =2.75, wspace=7)

#%%
plt.figure(2)
correlation = data.corr()

sbs.heatmap(correlation,annot= True, cmap='coolwarm')

#%%
plt.figure(3)
sbs.scatterplot(data=data, x=data.time, y=data.temp, hue=data.speed, alpha=.5, edgecolor=None)