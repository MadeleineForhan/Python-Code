# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:46:07 2022

@author: mmforhan
"""

import matplotlib.pyplot as plt
import pandas as pd  # (this is for reading a csv file)
from pandas import DataFrame as df
import datetime as dt
import numpy as np
import matplotlib.dates as mdates
import glob
import os
import seaborn as sns
#%%
#read in files
file= 'C:/Users/mmfor/Downloads/Python Data Sets/Spotify 2010 - 2019 Top 100.csv'
header=['title','artist','genre','year','added','bpm','energy','dance','decibel','live','val','duration','acous','speech','pop','topyear','artisttype']
dataold=pd.read_csv(file,names=header,skiprows=1,header= None)
data=pd.read_csv(file,names=header,skiprows=1,header= None, usecols=[3,5,6,7,8,9,10,11,12,13,14,15]) #usecols=[3,5,6,7,8,9,10,11,12,13,14,15]


#denergy lives!!
newdata = pd.DataFrame(data)

newdata['denergy'] = newdata['dance']/newdata['energy']

dataold['Genre Original'] = dataold['genre']


#Denergy but make it genre
new2=pd.DataFrame(dataold)
new2['denergy']=new2['dance']/new2['energy']

#%%
'''
sns.set(font_scale=1)
plt.figure()
sns.histplot(data=data,x=data.year)
plt.xlabel('Year Released')
plt.ylabel('Count')
plt.title('Release Year for all Top Songs from 2010-2019')
#%%
correlation=data.corr()
plt.figure()
sns.heatmap(data=correlation,annot = True, vmin=-1,vmax=1)
plt.title('Correlation Map of Top Song Factors')

#%%
#distribution data for year released vs top year

sns.displot(data=data,x=data.topyear,hue=data.year,hue_norm=(2009,2021),palette='rainbow',multiple='stack',height=10)
plt.title('Top Year and Year Written')
#%%

sns.displot(x=data.decibel,y=data.energy, kind='kde', rug = True)
'''
#%%
'''
Search and replace the genre names with more generic versions (Ex. 'electro pop' to 'pop') 
'''
dataold.genre.fillna('',inplace=True)
dataold.loc[dataold.genre.str.contains('rap'),'genre']='rap'
dataold.loc[dataold.genre.str.contains('hip hop'),'genre']='hip hop'
dataold.loc[dataold.genre.str.contains('rock'),'genre']='rock'
dataold.loc[dataold.genre.str.contains('dance|disco'),'genre']='dance/disco'
dataold.loc[dataold.genre.str.contains('indie'),'genre']='indie'
dataold.loc[dataold.genre.str.contains('country'),'genre']='country'
dataold.loc[dataold.genre.str.contains('r&b'),'genre']='R&B'
dataold.loc[dataold.genre.str.contains('contemporary'),'genre']='contemporary'
dataold.loc[dataold.genre.str.contains('pop'),'genre']='pop'
dataold.loc[~dataold.genre.str.contains('pop|rap|hip hop|rock|dance/disco|indie|country|R&B|contemporary'),'genre']='miscellaneous'

colors={'rap':'red','hip hop':'orange','rock':'yellow','dance/disco':'green','indie':'blue','country':'purple','R&b':'pink','contemportary':'grey','pop':'black','miscellaneous':'saddlebrown'}
#%%

data10 = dataold[dataold.topyear == 2010]
data11 = dataold[dataold.topyear == 2011]
data12 = dataold[dataold.topyear == 2012]
data13 = dataold[dataold.topyear == 2013]
data14 = dataold[dataold.topyear == 2014]
data15 = dataold[dataold.topyear == 2015]
data16 = dataold[dataold.topyear == 2016]
data17 = dataold[dataold.topyear == 2017]
data18 = dataold[dataold.topyear == 2018]
data19 = dataold[dataold.topyear == 2019]

#%%




#%%
'''
Search and replace the genre names with more generic versions (Ex. 'electro pop' to 'pop') 
'''
dataold.genre.fillna('',inplace=True)
dataold.loc[dataold.genre.str.contains('rap'),'genre']='rap'
dataold.loc[dataold.genre.str.contains('hip hop'),'genre']='hip hop'
dataold.loc[dataold.genre.str.contains('rock'),'genre']='rock'
dataold.loc[dataold.genre.str.contains('dance|disco'),'genre']='dance/disco'
dataold.loc[dataold.genre.str.contains('indie'),'genre']='indie'
dataold.loc[dataold.genre.str.contains('country'),'genre']='country'
dataold.loc[dataold.genre.str.contains('r&b'),'genre']='R&B'
dataold.loc[dataold.genre.str.contains('contemporary'),'genre']='contemporary'
dataold.loc[dataold.genre.str.contains('pop'),'genre']='pop'
dataold.loc[~dataold.genre.str.contains('pop|rap|hip hop|rock|dance/disco|indie|country|R&B|contemporary'),'genre']='miscellaneous'

colors={'rap':'red','hip hop':'orange','rock':'yellow','dance/disco':'green','indie':'blue','country':'purple','R&b':'pink','contemportary':'grey','pop':'black','miscellaneous':'saddlebrown'}

#%%
datarap = dataold[dataold.genre == 'rap']
datahh = dataold[dataold.genre == 'hip hop']
datarock = dataold[dataold.genre == 'rock']
datadance = dataold[dataold.genre == 'dance/disco']
dataindie = dataold[dataold.genre == 'indie']
datacountry = dataold[dataold.genre == 'country']
datarb = dataold[dataold.genre == 'R&B']
datacont = dataold[dataold.genre == 'contemporary']
datapop = dataold[dataold.genre == 'pop']
datamisc = dataold[dataold.genre == 'miscellaneous']
#%%
#%%
sns.set(font_scale=.8)
plt.figure(1)
plt.subplot(3,3,1)
sns.boxplot( x=data.topyear, y=data.bpm,palette='rainbow')
plt.subplot(3,3,2)
sns.boxplot(x=data.topyear,y=data.energy,palette='rainbow')
plt.subplot(3,3,3)
sns.boxplot(x=data.topyear,y=data.dance,palette='rainbow')
plt.subplot(3,3,4)
sns.boxplot(x=data.topyear,y=data.decibel,palette='rainbow')
plt.subplot(3,3,5)
sns.boxplot(x=data.topyear,y=data.live,palette='rainbow') 
plt.subplot(3,3,6)
sns.boxplot(x=data.topyear,y=data.val,palette='rainbow')
plt.subplot(3,3,7)
sns.boxplot(x=data.topyear,y=data.duration,palette='rainbow')
plt.subplot(3,3,8)
sns.boxplot(x=data.topyear,y=data.acous,palette='rainbow')
plt.subplot(3,3,9)
sns.boxplot(x=data.topyear,y=data.speech,palette='rainbow')

#%%
sns.set(font_scale=.8)
plt.figure()
plt.subplot(2,1,1)
sns.histplot(data=dataold,x='genre',multiple='dodge',hue='topyear',shrink=.8,palette='rainbow') #top year where it was na was replace with a blank due to our previous code. Help
plt.title('Genres of Top 100 Songs with Top Year')

plt.subplot(2,1,2)
sns.histplot(data=dataold,x='artisttype',multiple='dodge',hue='topyear',shrink=.8,palette='rainbow') #top year where it was na was replace with a blank due to our previous code. Help
plt.title('Artist Type of 100 Top Songs 2010-2019')
#sns.histplot(data=dataold.genre,stat='percent',discrete=True)

#%%
'''
'''
#Here begins the 'what the fuck 2013?' section of this code
'''
plt.figure()
plt.subplot(4,2,1)
plt.scatter(data13.energy,data13.bpm)
plt.title('energy/bpm')
plt.subplot(4,2,2)
plt.scatter(data13.energy,data13.duration)
plt.title('energy/duration')
plt.subplot(4,2,3)
plt.scatter(data13.energy,data13.dance)
plt.title('energy/dance')
plt.subplot(4,2,4)
plt.scatter(data13.energy,data13.decibel)
plt.title('energy/decibel')
#Energy vs decibel level has a mild positive correlation
plt.subplot(4,2,5)
plt.scatter(data13.energy,data13.live)
plt.title('energy/liveliness')
plt.subplot(4,2,6)
plt.scatter(data13.energy,data13.val)
plt.title('energy/val')
plt.subplot(4,2,7)
plt.scatter(data13.energy,data13.acous)
plt.title('energy/acous')
plt.subplot(4,2,8)
plt.scatter(data13.energy,data13.speech)
plt.title('energy/speech')
'''
#%%
#brief aside from wtf 2013? 

dataquiet=data[data.decibel > -5]
dataloud=data[data.decibel < -3]

correlationq=dataquiet.corr()
correlationl=dataloud.corr()
plt.figure()
plt.subplot(1,2,1)
sns.heatmap(data=correlationq,annot=True,vmin=-1,vmax=1)
plt.title('Quiet')
plt.subplot(1,2,2)
sns.heatmap(data=correlationl,annot=True,vmin=-1,vmax=1)
plt.title('loud')
#conclusion: deicbel does not determine the energy on quiet music but, it does determine the energy on loud music.
#%%
#pair plots by beloved
#sns.pairplot(data=data) do not run Sarah, it hurts your computer
#year vs energy colored with dance
plt.figure()
plt.scatter(data.topyear, data.energy, c=data.dance)
plt.colorbar()
#%%
plt.figure()
plt.scatter(data.topyear, data.energy, c=data.val)
#%%
plt.figure()
plt.scatter(data.energy,data.dance, c=data.topyear,cmap='gist_ncar')
plt.colorbar()

#%%
sns.kdeplot(data=data,x=data.energy,y=data.dance, hue=data.topyear)
#%%
plt.figure()
plt.subplot(2,5,1)
sns.kdeplot(data=data10,x=data10.energy,y=data10.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,2)
sns.kdeplot(data=data11,x=data11.energy,y=data11.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,3)
sns.kdeplot(data=data12,x=data12.energy,y=data12.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,4)
sns.kdeplot(data=data13,x=data13.energy,y=data13.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,5)
sns.kdeplot(data=data14,x=data14.energy,y=data14.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,6)
sns.kdeplot(data=data15,x=data15.energy,y=data15.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,7)
sns.kdeplot(data=data16,x=data16.energy,y=data16.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,8)
sns.kdeplot(data=data17,x=data17.energy,y=data17.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,9)
sns.kdeplot(data=data18,x=data18.energy,y=data18.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,10)
sns.kdeplot(data=data19,x=data19.energy,y=data19.dance)
plt.xlim((0,110))
plt.ylim((0,110))
#pull out kde plot for each year and compare.

#%%
plt.figure()
plt.subplot(2,5,1)
plt.title('rap')
sns.kdeplot(data=datarap,x=datarap.energy,y=datarap.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,2)
plt.title('hip hop')
sns.kdeplot(data=datahh,x=datahh.energy,y=datahh.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,3)
plt.title('rock')
sns.kdeplot(data=datarock,x=datarock.energy,y=datarock.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,4)
plt.title('dance')
sns.kdeplot(data=datadance,x=datadance.energy,y=datadance.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,5)
plt.title('indie')
sns.kdeplot(data=dataindie,x=dataindie.energy,y=dataindie.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,6)
plt.title('country')
sns.kdeplot(data=datacountry,x=datacountry.energy,y=datacountry.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,7)
plt.title('R&B')
sns.kdeplot(data=datarb,x=datarb.energy,y=datarb.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,8)
plt.title('contemporary')
sns.kdeplot(data=datacont,x=datacont.energy,y=datacont.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,9)
plt.title('pop')
sns.kdeplot(data=datapop,x=datapop.energy,y=datapop.dance)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,10)
plt.title('misc')
sns.kdeplot(data=datamisc,x=datamisc.energy,y=datamisc.dance)
plt.xlim((0,110))
plt.ylim((0,110))
#pull out genre for energy and dance and compare
#%%
plt.figure()
plt.subplot(2,5,1)
sns.scatterplot(data=data10,x=data10.energy,y=data10.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,2)
sns.scatterplot(data=data11,x=data11.energy,y=data11.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,3)
sns.scatterplot(data=data12,x=data12.energy,y=data12.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,4)
sns.scatterplot(data=data13,x=data13.energy,y=data13.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,5)
sns.scatterplot(data=data14,x=data14.energy,y=data14.dance,hue=dataold.genre)
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left', borderaxespad=0)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,6)
sns.scatterplot(data=data15,x=data15.energy,y=data15.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,7)
sns.scatterplot(data=data16,x=data16.energy,y=data16.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,8)
sns.scatterplot(data=data17,x=data17.energy,y=data17.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,9)
sns.scatterplot(data=data18,x=data18.energy,y=data18.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
plt.subplot(2,5,10)
sns.scatterplot(data=data19,x=data19.energy,y=data19.dance,hue=dataold.genre,legend=False)
plt.xlim((0,110))
plt.ylim((0,110))
#Scatterplots of dance and energy by year colored with dance
#%%
sns.set(font_scale=.8)
plt.figure()
plt.subplot(3,3,1)
sns.boxplot( x=dataold.genre, y=dataold.bpm,palette='terrain')
plt.subplot(3,3,2)
sns.boxplot( x=dataold.genre, y=dataold.energy,palette='terrain')
plt.subplot(3,3,3)
sns.boxplot( x=dataold.genre, y=dataold.dance,palette='terrain')
plt.subplot(3,3,4)
sns.boxplot( x=dataold.genre, y=dataold.decibel,palette='terrain')
plt.subplot(3,3,5)
sns.boxplot( x=dataold.genre, y=dataold.live,palette='terrain')
plt.subplot(3,3,6)
sns.boxplot( x=dataold.genre, y=dataold.val,palette='terrain')
plt.subplot(3,3,7)
sns.boxplot( x=dataold.genre, y=dataold.duration,palette='terrain')
plt.subplot(3,3,8)
sns.boxplot( x=dataold.genre, y=dataold.acous,palette='terrain')
plt.subplot(3,3,9)
sns.boxplot( x=dataold.genre, y=dataold.speech,palette='terrain')

#%%
'''
next step Denergy! Dance/energy compared to top year or type. Create denergy by adding extra column to data set that is the dance value over the energy value.
Look at first cell, denergy is alive!!!!
'''
plt.figure()
plt.scatter(newdata.denergy, newdata.topyear)
#%%
plt.figure()
plt.subplot(2,4,1)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.bpm)
plt.subplot(2,4,2)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.decibel)
plt.subplot(2,4,3)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.live)
plt.subplot(2,4,4)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.val)
plt.subplot(2,4,5)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.duration)
plt.subplot(2,4,6)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.acous)
plt.subplot(2,4,7)
sns.kdeplot(data=newdata,x=newdata.denergy,y=newdata.speech)
#%%%
plt.figure()
plt.hist(newdata.denergy,bins=75)

plt.figure()
sns.boxplot(x=newdata.denergy)
#%%
plt.figure()
sns.violinplot(x=new2.topyear,y=new2.denergy)
plt.ylim((0,4))
plt.figure()
sns.violinplot(x=new2.genre, y=new2.denergy)
plt.ylim((0,4))
#%%
plt.figure()
plt.subplot(2,1,1)
sns.boxplot(x=new2.topyear,y=new2.denergy)
plt.subplot(2,1,2)
sns.boxplot(x=new2.genre, y=new2.denergy)
#%%
plt.figure()
plt.subplot(2,5,1)
plt.title('rap')
sns.boxplot(x=datarap.topyear, y=datarap.denergy)
plt.ylim((0,4))
plt.subplot(2,5,2)
plt.title('hip hop')
sns.boxplot(x=datahh.topyear, y=datahh.denergy)
plt.ylim((0,4))
plt.subplot(2,5,3)
plt.title('rock')
sns.boxplot(x=datarock.topyear,y= datarock.denergy)
plt.ylim((0,4))
plt.subplot(2,5,4)
plt.title('dance/disco')
sns.boxplot(x=datadance.topyear, y=datadance.denergy)
plt.ylim((0,4))
plt.subplot(2,5,5)
plt.title('indie')
sns.boxplot(x=dataindie.topyear, y=dataindie.denergy)
plt.ylim((0,4))
plt.subplot(2,5,6)
plt.title('country')
sns.boxplot(x=datacountry.topyear, y=datacountry.denergy)
plt.ylim((0,4))
plt.subplot(2,5,7)
plt.title('R&B')
sns.boxplot(x=datarb.topyear, y=datarb.denergy)
plt.ylim((0,4))
plt.subplot(2,5,8)
plt.title('pop')
sns.boxplot(x=datapop.topyear, y=datapop.denergy)
plt.ylim((0,4))
plt.subplot(2,5,9)
plt.title('misc')
sns.boxplot(x=datamisc.topyear, y=datamisc.denergy)
plt.ylim((0,4))