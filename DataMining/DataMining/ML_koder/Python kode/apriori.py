# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:19:06 2022

@author: gamer
"""

#%%

from sklearn.cluster import k_means

def apriori_candidate_generation(itemsets):
    # itemsets: list of itemsets
    # return: list of candidate itemsets
    
    # initialize
    candidates = []
    # sort itemsets by length
    itemsets.sort(key=lambda x: len(x))
    # loop over itemsets
    for i in range(len(itemsets)):


        print(apriori_candidate_generation(itemsets))



itemsets = [[1,2,3]]

apriori_candidate_generation(itemsets)

#%%
