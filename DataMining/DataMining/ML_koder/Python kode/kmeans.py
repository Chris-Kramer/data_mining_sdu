# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:23:42 2022

@author: gamer
"""
#%%

def kmeans(points, initial_means):
    num_clusters = len(initial_means)
    
    for i in points:
        distance1 = abs(i - initial_means[0])
        distance2 = abs(i - initial_means[1])
        print("Distance from point " + str(i) + " to cluster " + str(initial_means[0]) + " is " + str(distance1))
        print("Distance from point " + str(i) + " to cluster " + str(initial_means[1]) + " is " + str(distance2))

kmeans([2,3,4,10,11,12,20,25,30], [2,6])


#%%

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[5,3],
     [1,3],
     [1,8],
     [1,9],
     [4,6],
     [5,4],
     [5,7],
     [6,1],
     [6,3],
     [6,6],
     [6,8],
     [7,2],
     [7,4],
     [7,6],
     [8,2],
     [8,3],
 ])

kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
print(kmeans.labels_)
#print(kmeans.predict(np.array([[6,6]])))
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow', s=100)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(which='both')
plt.show()


#%%

