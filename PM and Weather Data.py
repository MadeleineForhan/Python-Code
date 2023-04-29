# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:01:17 2022

@author: mmfor
"""

import matplotlib.pyplot as plt
import pandas as pd  # (this is for reading a csv file)
import datetime as dt
import seaborn as sns



filePA='C:/Users/mmfor/Downloads/Python Data Sets/Water Street Keene 1_1_2018 12_31_2018 A.csv'


fileW='C:/Users/mmfor/Downloads/Python Data Sets/modified_EEN-2018.csv'

outfile='C:/Users/mmfor/Downloads/Python Data Sets/WATERSTREETresamplePAandWthrMETARSNOW-2018.csv'


##########################
#read in the data

PAdata=pd.read_csv(filePA,usecols=[0,9],names=['created_at','PM25'],skiprows=1,header=None)

Wdata=pd.read_csv(fileW, usecols=[0,1,2,3,5,6,8,28])

#change the column headers
Wdata = Wdata.rename( columns={'tmpf':'temp', 'dwpf':'dewpoint', 'relh':'RH' ,  'sknt':'windspeed', 'p01i':'precip'}    )


########################
#datetimes

#----------------------
#Date times for the PA
#---------------------

#for A data
numptsA=PAdata.created_at.shape[0]
date_dt=[0 for i in range(numptsA)]

for t in range(0,numptsA):
    tempdate=PAdata.created_at[t]
    date_dt[t]=dt.datetime.strptime(tempdate, '%Y-%m-%d %H:%M:%S UTC') #UTC
   
#Put PA in pandas
PAdata['datetime']=date_dt





#----------------------
#Date times for the Weather
#----------------------
numptsW=Wdata.Date.shape[0]
date_dtW=[0 for i in range(numptsW)]
for t in range(0,numptsW): #error in last element
    tempdate=Wdata.Date[t]
    date_dtW[t]=dt.datetime.strptime(tempdate, '%Y-%m-%d %H:%M:%S')
   
#Put into pandas
Wdata['datetime']=date_dtW

#%%
#make the index be the date times

PAdata2=PAdata.set_index('datetime')
PAdata3=PAdata2.sort_index()

#drop first parts of weather data

Wdata=Wdata.drop(Wdata.index[0:16600])
Wdata2=Wdata.set_index('datetime')
Wdata2=Wdata2.sort_index()

#reset the weather data to the same time as PM data

Wdata3=Wdata2.reindex(index=PAdata2.index, method='nearest')

#merge data

ALLdata=pd.merge(PAdata2,Wdata3,left_index=True, right_index=True)
ALLdata=ALLdata.reset_index()