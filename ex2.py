#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 08:33:21 2018

@author: daegonny
"""
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

NUMBER_POINTS =  100
EPOCHS = 500
ALPHA = 0.01

x = [-2 + n*(4/(NUMBER_POINTS-1)) for n in range(NUMBER_POINTS)]
y = [xi*xi for xi in x]

plt.plot(x,y)

#partições fuzzy gaussianas
m1 = 1
s1 = 0.5

def w1(x):
    return np.exp(-0.5*np.power((x-m1)/(s1),2))

m2 = -1
s2 = 0.5

def w2(x):
    return np.exp(-0.5*np.power((x-m2)/(s2),2))


w1_pred = [w1(xi) for xi in x]
w2_pred = [w2(xi) for xi in x]
plt.plot(x,w1_pred,x, w2_pred)

#equações paramétricas
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
z_pred = [z(xi) for xi in x]

#plt.plot(x,z_pred,x, y)


#derivadas parciais de z

def del_m1(x):
    return w2(x) * ((z1(x) - z2(x))/np.power((w1(x) + w2(x)),2)) * w1(x) * ((x-m1)/np.power(s1,2))

def del_m2(x):
    return w1(x) * ((z2(x) - z1(x))/np.power((w1(x) + w2(x)),2)) * w2(x) * ((x-m2)/np.power(s2,2))

def del_s1(x):
    return w2(x) * ((z1(x) - z2(x))/np.power((w1(x) + w2(x)),2)) * w1(x) * (np.power((x-m1),2)/np.power(s1,3))

def del_s2(x):
    return w1(x) * ((z2(x) - z1(x))/np.power((w1(x) + w2(x)),2)) * w2(x) * (np.power((x-m1),2)/np.power(s2,3))

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
        s1 = s1 + (error*ALPHA*del_s1(x[idx]))
        s2 = s2 + (error*ALPHA*del_s2(x[idx]))
        m1 = m1 + (error*ALPHA*del_m1(x[idx]))
        m2 = m2 + (error*ALPHA*del_m2(x[idx]))
        
    
    errors.append(total_error)
    epoch += 1


y_pred = [z(xi) for xi in x]

plt.plot(x, y,x,y_pred)
plt.show()
plt.plot(errors)