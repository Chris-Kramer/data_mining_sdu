# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 22:01:14 2022

@author: gamer
"""

def g(a,b):
    sum = (a+b)**2
    return 1 - (((a**2)/sum) + ((b**2)/sum))

def gini(a,b,c,d):
    #print(a+b)
    #print(a+b+c+d)
    #print(g(a,b))
    return (((a+b)/(a+b+c+d))*g(a,b)) + (((c+d)/(a+b+c+d)) * g(c,d))

print(gini(1,2,1,1))

#short, lil finger 0.25
#short, fate 0.333
#long, lil finger 0.333
#long, fate 0.266

