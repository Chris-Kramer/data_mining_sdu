# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:57:53 2022

@author: gamer
"""

from sklearn.neighbors import LocalOutlierFactor, NearestNeighbors
from scipy.spatial import distance

data = [(1,7),(3,4),(3,7),(4,6),(4,7),(5,2),(5,5),(6,6)]
# point to calculate LOF for
p = (3, 4)
knn = NearestNeighbors(n_neighbors=2,algorithm="auto",metric="cityblock")
knn.fit(data)
print(knn.kneighbors(data))
#print(data)