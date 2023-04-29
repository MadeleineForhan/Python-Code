# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:03:04 2022

@author: mmfor
"""
#Images are just visual datasets
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import PIL
#%%
''' 
data=np.zeros((100,70))
#data[0,2]=3 #puts 3 into the zero row and 2nd column (like (x,y))
data[80,35]=50
data[35,45:55]=-50
data[35,15:25]=-50
data[36,18:21]=-15
data[36,48:51]=-15
data[37,19:21]=-15
data[37,49:50]=-15
data[55,30:40]=-50
data[80,20:51]=20

mindex2=[79,79,78,78,77,77]
mindex3=[19,51,18,52,17,53]

data[mindex2,mindex3]=20

plt.imshow(data,cmap='afmhot_r')
'''
#%%
file='C:/Users/mmfor/Downloads/Python Data Sets/sunblank.jpg'
#open the image
sun = PIL.Image.open(file)
sun = sun.convert('RGB')
sun2=sun.convert('CMYK')
#to convert to grey scale use 'L'
#to convert to CMYK use 'CMYK'

data = np.array(sun)
data2 =np.array(sun2)
#data.shape gives array
redchannel=data[:,:,0]
greenchannel=data[:,:,1]
bluechannel=data[:,:,2]

cchannel=data2[:,:,0]
mchannel=data2[:,:,1]
ychannel=data2[:,:,2]
kchannel=data2[:,:,3]
#%%
#make image
plt.figure()
plt.subplot(2,4,1)
plt.imshow(sun)

plt.subplot(2,4,2)
plt.imshow(redchannel, cmap='Reds',vmin=0, vmax=255)
plt.title('Red Channel')
plt.subplot(2,4,3)
plt.imshow(greenchannel, cmap='Greens',vmin=0, vmax=255)
plt.title('Green Channel')
plt.subplot(2,4,4)
plt.imshow(bluechannel,cmap='Blues',vmin=0, vmax=255)
plt.title('Blue Channel')

plt.subplot(2,4,5)
plt.imshow(cchannel,cmap='YlGnBu',vmin=0,vmax=255)
plt.title('Cyan Channel')
plt.subplot(2,4,6)
plt.imshow(mchannel,cmap='RdPu',vmin=0,vmax=255)
plt.title('Magenta Channel')
plt.subplot(2,4,7)
plt.imshow(ychannel,cmap='YlOrBr',vmin=0,vmax=255)
plt.title('Yellow Channel')
plt.subplot(2,4,8)
plt.imshow(kchannel,cmap='binary',vmin=0,vmax=255)
plt.title('Black Channel')
#%%
#recreate an image
data[60:150,100:150,0] = data[60:150,100:150,0]-150
sun3=PIL.Image.fromarray(data)
plt.imshow(sun3)