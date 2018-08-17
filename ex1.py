#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:33:21 2018

@author: daegonny
"""
#import numpy as np
#import matplotlib.pyplot as plt

NUMBER_POINTS =  12

x=[
   -0.91, 
   -0.77,
   -0.44,
   -0.39,
   -0.21,
   -0.01,
   0.22,
   0.33,
   0.47,
   0.65,
   0.85,
   0.89
]

y = [
     0.9101,
     0.6469,
     0.1816,
     0.1301,
     -0.0139,
     -0.0979,
     -0.0956,
     -0.0571,
     0.0269,
     0.1925,
     0.4525,
     0.5141
 ]

#plt.scatter(x,y)


#partições fuzzy

a1 = -1
b1 = 0
def  w1(x):
    return a1*x + b1

a2 = 1
b2 = 0
def  w2(x):
    return a2*x + b2


#equações paramétricas
    
p1 = 2
r1 = 0
def z1(x):
    return p1*x + r1

p2 = -2
r2 = 0
def z2(x):
    return p2*x + r2

#média ponderada 
    
def z(x):
    (w1(x)*z1(x) + w2(x)*z2(x))/ (w1(x)/w2(x)) 


