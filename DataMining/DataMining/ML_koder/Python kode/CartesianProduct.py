# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:30:47 2022

@author: gamer
"""

def CartesianProduct(set1, set2):
    print("CARTESIAN PRODUCT OF:")
    print("AxB = {", end="")
    for i in range(len(set1)):
        for j in range(len(set2)):
            print("(",set1[i],",",set2[j],")", end ="")
    print("}")

#def BinaryRelation(set1, set2):

if __name__ == "__main__":
    set1 = ("a","b","c") #set1
    set2 = (1,2,3,4) #set2

    CartesianProduct(set1,set2)