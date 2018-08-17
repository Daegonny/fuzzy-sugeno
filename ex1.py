#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:33:21 2018

@author: daegonny
"""
#import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

NUMBER_POINTS =  12
EPOCHS = 500
ALPHA = 000.1

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


#partições fuzzy com valores arbitrários

a1 = -0.5
b1 = 0.1
def  w1(x):
    return (a1*x + b1)

a2 = 0.7
b2 = -0.1
def  w2(x):
    return (a2*x + b2)


#equações paramétricas com valores de retas arbitrárias
    
p1 = 0.1
r1 = 0.3
def z1(x):
    return (p1*x + r1)

p2 = -0.1
r2 = -0.2
def z2(x):
    return (p2*x + r2)

#média ponderada 
    
def z(x):
    num = w1(x)*z1(x) + w2(x)*z2(x)
    den = w1(x)+w2(x)
    return num/den



#comparação das duas parábolas antes da otimização
y_pred = [z(xi) for xi in x]

plt.plot(x,y_pred,x, y)
plt.show()

#derivadas parciais de z
def del_a1(x):
    return w1(x)*x/(w1(x)+w2(x))

def del_a2(x):
    return w2(x)*x/(w1(x)+w2(x))

def del_b1(x):
    return w1(x)/(w1(x)+w2(x))

def del_b2(x):
    return w2(x)/(w1(x)+w2(x))

def del_p1(x):
    return w1(x)*x/(w1(x)+w2(x))

def del_p2(x):
    return w2(x)*x/(w1(x)+w2(x))

def del_r1(x):
    return w1(x)/(w1(x)+w2(x))

def del_r2(x):
    return w2(x)/(w1(x)+w2(x))


#lista de indices que pode ser embaralhada aleatoriamente
indexes = list(range(NUMBER_POINTS))

#treinamento
epoch = 0
errors = []
while epoch < EPOCHS:
    shuffle(indexes)
    total_error = 0
    for idx in indexes:
        y_pred = z(x[idx])
        error = y[idx] - y_pred 
        
        total_error += error
        
        #ajuste
        p1 = p1 + (error*ALPHA*del_p1(x[idx]))
        p2 = p2 + (error*ALPHA*del_p2(x[idx]))
        r1 = r1 + (error*ALPHA*del_r1(x[idx]))
        r2 = r2 + (error*ALPHA*del_r2(x[idx]))
        a1 = a1 + (error*ALPHA*del_a1(x[idx]))
        a2 = a2 + (error*ALPHA*del_a2(x[idx]))
        b1 = b1 + (error*ALPHA*del_b1(x[idx]))
        b2 = b2 + (error*ALPHA*del_b2(x[idx]))
    
    errors.append(total_error)
    epoch += 1

#print(del_p1(x[0]))
y_pred = [z(xi) for xi in x]

plt.plot(x,y_pred,x, y)
plt.show()
