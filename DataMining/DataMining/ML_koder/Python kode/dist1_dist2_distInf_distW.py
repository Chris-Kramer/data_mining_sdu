# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:31:21 2022

@author: gamer
"""

import numpy as np

def calulcateAll(p, q):
    dist2 = 0
    dist1 = 0
    distInf = 0
    distW = 0
    #distM = 0
    w = [1,1.5,2.5] # Manipulate
    #M1 = np.matrix([[1,0,0], [0,1,0], [0,0,1]])
    #M2 = np.matrix([[1,0.9,0.7], [0.9,1,0.8], [0.7,0.8,1]])

    dist2 = ((abs(p[0]-q[0])**2)+(abs(p[1]-q[1])**2)+(abs(p[2]-q[2])**2))**(1/2)
    dist1 = (abs(p[0]-q[0]))+(abs(p[1]-q[1]))+(abs(p[2]-q[2]))
    distinf = max((abs(p[0]-q[0])),(abs(p[1]-q[1])),(abs(p[2]-q[2])))
    distw = ((w[0]*abs(p[0]-q[0])**2)+(w[1]*abs(p[1]-q[1])**2)+(w[2]*abs(p[2]-q[2])**2))**(1/2)
    #distM = np.sqrt(np.dot((p-q),M1))(p-q).t
    
    print("----------------")
    print("dist2 = ", dist2)
    print("----------------")
    print("dist1 = ", dist1)
    print("----------------")
    print("distInf = ", distinf)
    print("----------------")
    print("distw = ", distw)
    print("----------------")


#a (1, 4, 4), b(8, 1, 7), c(2, 4, 10), d(1, 2, 13), q(1, 8, 7)\


if __name__ == "__main__":
    q = [4,7,8] # Manipulate
    p = [2,3,5] #  Manipulate
    calulcateAll(p,q)