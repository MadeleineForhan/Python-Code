#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:35:25 2022

@author: sm1009
"""


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
data0=pd.read_csv(filelist[0],names=columnHead,skiprows=1,header=None)


#IN ORDER TO PLOT
#
#get number of points for each file
numpts0=data0.DO.shape[0]
date_dt=[0 for i in range(numpts0)]


for i in range(0,numpts0):
    tempdate=data0.date[i]

    date_dt[i]=dt.datetime.strptime(tempdate, '%m/%d/%y %H:%M')
    
    
data0['datetime']=date_dt


plt.figure()
plt.plot(data0.datetime, data0.DO)

