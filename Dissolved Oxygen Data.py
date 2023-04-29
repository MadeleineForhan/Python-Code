# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:29:52 2022

@author: mmfor
"""
###Example Glob, reading in lots of Files

import matplotlib.pyplot as plt
import pandas as pd  # (this is for reading a csv file)
from pandas import DataFrame as df
import datetime as dt
import numpy as np
import matplotlib.dates as mdates
import glob
import os

#******************
# File 


filedir='C:/Users/mmfor/Downloads/Python Data Sets/'
filelist=glob.glob(filedir+'HC*.csv')

#%%
#--------------------------
#read in data


columnHead=['date','DO','Temp']

#Read in the data with the new columnHeaders


mydateparse= lambda x:pd.datetime.strptime(x, '%m/%d/%y %H:%M')

data0=pd.read_csv(filelist[0],names=columnHead,skiprows=1,header=None, parse_dates=[0],date_parser=mydateparse)
data1=pd.read_csv(filelist[1],names=columnHead,skiprows=1,header=None, parse_dates=[0],date_parser=mydateparse)
data2=pd.read_csv(filelist[2],names=columnHead,skiprows=1,header=None, parse_dates=[0],date_parser=mydateparse)
data3=pd.read_csv(filelist[3],names=columnHead,skiprows=1,header=None, parse_dates=[0],date_parser=mydateparse)

#%%
numpts0=data0.DO.shape[0]
numpts1=data1.DO.shape[0]
numpts2=data2.DO.shape[0]
numpts3=data3.DO.shape[0]
#%%
#Removing Bad Data
indx=np.where(data0.DO<0)[0]
data0.DO[indx]=np.nan
indx=np.where(data1.DO<0)[0]
data1.DO[indx]=np.nan
indx=np.where(data2.DO<0)[0]
data2.DO[indx]=np.nan
indx=np.where(data3.DO<0)[0]
data3.DO[indx]=np.nan

#%%
#finding labels
fn=os.path.split(filelist[0])[1]
location=fn.split('_')[0]
fn=os.path.split(filelist[1])[1]
fn=os.path.split(filelist[2])[1]
fn=os.path.split(filelist[3])[1]
#%%
LOClabel=[]
for i in range(0,4):
    fn = os.path.split(filelist[i])[1]
    location= fn.split('_')[0]
    LOClabel.append(location)
#%%
ax=plt.figure()

plt.plot(data0.date,data0.DO, label=LOClabel[0])
plt.plot(data1.date,data1.DO, label=LOClabel[1])
plt.plot(data2.date,data2.DO, label=LOClabel[2])
plt.plot(data3.date,data3.DO, label=LOClabel[3])


plt.xlabel('Date')
plt.ylabel('Dissolved Oxygen')
plt.legend()

plt.xlim((pd.Timestamp('2014-12-12'), pd.Timestamp('2015-05-01')))

#%%
#Setting index to detrend
'''
indx0=np.where((data0.date>=pd.Timestamp('2014-12-12')) & (data0.date <pd.Timestamp('2015-05-01')) & (np.isnan(data0.DO)==False) )[0]
indx1=np.where((data1.date>=pd.Timestamp('2014-12-12')) & (data1.date <pd.Timestamp('2015-05-01')) & (np.isnan(data1.DO)==False) )[0]
#indx2=np.where((data2.date>=pd.Timestamp('2015-01-01')) & (data2.date <pd.Timestamp('2015-04-01')) & (np.isnan(data2.DO)==False) )[0]  
indx3=np.where((data3.date>=pd.Timestamp('2014-12-12')) & (data3.date <pd.Timestamp('2015-05-01')) & (np.isnan(data3.DO)==False) )[0] 
'''
#%%
'''
from scipy import signal
y0=signal.detrend(data0.DO[indx0])
y1=signal.detrend(data1.DO[indx1])
#y2=signal.detrend(data2.DO[indx2])
y3=signal.detrend(data3.DO[indx3])
#%%

plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.plot(data0.date[indx0],data0.DO[indx0],label=LOClabel[0])
plt.plot(data1.date[indx1],data1.DO[indx1],label=LOClabel[1])
plt.plot(data3.date[indx3],data3.DO[indx3],label=LOClabel[3])
plt.xlabel('date')
plt.ylabel('Dissolved Oxygen')
plt.legend()
plt.subplot(2,1,2)
plt.plot(data0.date[indx0],y0,label='detrended'+LOClabel[0])
plt.plot(data1.date[indx1],y1,label='detrended'+LOClabel[1])
plt.plot(data3.date[indx3],y3,label='detrended'+LOClabel[3])
plt.xlabel('date')
plt.ylabel('Dissolved Oxygen')
plt.legend()
plt.show()
plt.suptitle('Dissolved Oxygen and Detrended Disssolved Oxyegn vs Date')
'''
#%%
#Rolling Average

RA0=data0.DO.rolling(1500,center=True).mean()
RA1=data1.DO.rolling(1500,center=True).mean()
RA3=data3.DO.rolling(1500,center=True).mean()
data0['detrend']=data0.DO-RA0
data1['detrend']=data1.DO-RA1
data3['detrend']=data3.DO-RA3

#%%
plt.figure(figsize=(10,5))



plt.subplot(2,1,1)
plt.plot(data0.date,data0.DO,label=LOClabel[0])
plt.plot(data1.date,data1.DO,label=LOClabel[1])
plt.plot(data3.date,data3.DO,label=LOClabel[3])

plt.plot(data0.date,RA0,linestyle='--',label='rolling '+LOClabel[0])
plt.plot(data1.date,RA1,linestyle='--',label='rolling '+LOClabel[1])
plt.plot(data3.date,RA3,linestyle='--',label='rolling '+LOClabel[3])
plt.xticks([])
plt.ylabel('Dissolved Oxygen')
plt.xlim((pd.Timestamp(year=2014, month=12, day=1),pd.Timestamp(year=2015, month=5, day=1)))
plt.legend()







plt.subplot(2,1,2)
plt.plot(data0.date,data0.detrend,label='detrended '+LOClabel[0])
plt.plot(data1.date,data1.detrend,label='detrended' + LOClabel[1])
plt.plot(data3.date,data3.detrend,label='detrended' + LOClabel[3])
plt.xlabel('date')
plt.ylabel('Dissolved Oxygen')
plt.xlim((pd.Timestamp(year=2014, month=12, day=1),pd.Timestamp(year=2015, month=5, day=1)))
#plt.title('removing the rolling average')
plt.legend()

#adjusting plots now. 
plt.subplots_adjust(wspace=0, hspace=0)

#%%
#figure with double axis
plt.figure(figsize=(10,5))
ax1=plt.subplot(1,1,1)
plt.plot(data1.date,data1.DO,'-',color='rebeccapurple')
plt.ylabel('Dissolved Oxygen',color='rebeccapurple')
plt.xlim((pd.Timestamp(year=2014, month=12, day=1),pd.Timestamp(year=2015, month=5, day=1)))
plt.text(pd.Timestamp(year=2014, month=12, day=1),15,LOClabel[1],fontsize=30,fontfamily='fantasy')

#define second axis
ax2=ax1.twinx()
plt.plot(data1.date,data1.Temp,'.',color='green')
plt.ylabel('temperature', color='green')
plt.ylim(-1,30)

#%%
#same info but scatter plot
plt.figure
plt.scatter(data1.date,data1.DO,c=data1.Temp,vmin=-1,vmax=15, cmap='RdYlBu_r')
plt.xlim((pd.Timestamp(year=2014, month=12, day=1),pd.Timestamp(year=2015, month=5, day=1)))
plt.colorbar()
#%%
#What hour is it? Day or night?
import matplotlib.colors as mcolors
hours= data1.date.dt.hour + data1.date.dt.minute/60
colors1=plt.cm.terrain( np.linspace(0,0.5,100)  ) #0 is start and .5 is % (grabbed 50% of cmap)
#cmaps have 256 slots to put colors in 128 is half
colors2=plt.cm.terrain_r( np.linspace(.5,1,100))
#stitching
colors=np.vstack((colors1,colors2))
mymap=mcolors.LinearSegmentedColormap.from_list('my_colormap',colors)



plt.figure()
plt.scatter(data1.date,data1.DO-RA1,c=hours, cmap=mymap)
plt.xlim((pd.Timestamp(year=2014, month=12, day=1),pd.Timestamp(year=2015, month=5, day=1)))
plt.colorbar()
plt.ylabel('Dissolved Oxygen')
plt.xlabel('Datetime')