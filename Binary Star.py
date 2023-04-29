# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:01:02 2022

@author: mmfor
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import PIL
import matplotlib.patches as patches
#%%
file='C:/Users/mmfor/Downloads/Binary01.jpg'
binary=PIL.Image.open(file)
binary=binary.convert('L')



#%%
plt.imshow(binary,cmap='bone')
plt.grid(False)

#%%
plt.figure()
plt.grid(False)
ax1=plt.subplot(1,1,1)

ax1.imshow(binary,cmap='bone')
#create the patch
rect=patches.Rectangle((2900,1125),250,250,linewidth=2,edgecolor='hotpink',facecolor='none')
ax1.add_patch(rect)

#%%
#crop image
#top point coord (2900,1125), bottom point coord (3150,1350)
binary2=binary.crop((2900,1125,3150,1350))

plt.figure('cropped figure')
plt.imshow(binary2,cmap='bone')


databin=np.array(binary2)

#%%
#create grid

xx,yy=np.mgrid[0:databin.shape[0],0:databin.shape[1]]

#create a 3d surface figure
fig=plt.figure()
ax = fig.gca(projection='3d')

#plot
surf=ax.plot_surface(xx,yy,databin,linewidth=0,antialiased=False,color='deeppink')
#%%
plt.figure(2)
plt.contour(databin,[33])
plt.show
#%%

def centermass (X):
    x=X[:,0]
    y=X[:,1]
    g=(x[:-1]*y[1:]-x[1:]*y[:-1])
    A=0.5*g.sum()
    cx=((x[:-1]+x[1:])*g).sum()
    cy=((y[:-1]+y[1:])*g).sum()
    return 1./(6*A)*np.array([cx,cy])

fig,ax=plt.subplots()
ax.pcolormesh(xx,yy,databin)
contr=ax.contour(xx,yy,databin,levels=[50],colors='k')

c0=centermass(contr.allsegs[0][0])
c1=centermass(contr.allsegs[0][1])

ax.plot(c0[0],c0[1],marker='.',markersize=8,color='deeppink')
ax.plot(c1[0],c1[1],marker='.',markersize=8,color='deeppink')

distance=np.sqrt((c0[0]-c1[0])**2+(c0[1]-c1[1])**2)
print(distance)
#%%
#put images into subplots
plt.figure()
plt.subplot(2,1,1)
plt.imshow(binary)
ax1=plt.subplot(2,1,1)

ax1.imshow(binary,cmap='bone')
#create the patch
rect=patches.Rectangle((2900,1125),250,250,linewidth=2,edgecolor='hotpink',facecolor='none')
ax1.add_patch(rect)

plt.subplot(2,1,2)
ax=plt.subplot(2,1,2)
ax.pcolormesh(xx,yy,databin)
contr=ax.contour(xx,yy,databin,levels=[50],colors='k')

c0=centermass(contr.allsegs[0][0])
c1=centermass(contr.allsegs[0][1])

ax.plot(c0[0],c0[1],marker='.',markersize=8,color='deeppink')
ax.plot(c1[0],c1[1],marker='.',markersize=8,color='deeppink')

plt.title('Distance of Binary Stars: 52.91988 Pixels')
