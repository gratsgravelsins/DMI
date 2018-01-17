# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def mans_j1(x):
    k = 0
    a = (-1)**0*x**1/(1)
    s = a
    while k<500:
        k = k + 1
        #R = (-1) * x**2/((2*k)*(2*k+1))
        R = (-1) * x**2/((4*k)*(k+1))
        a = a * R
        s = s + a
        
    return s

a = 0
b = 3* np.pi   #4.71 
x = np.arange(a,b,0.05)
y = mans_j1(x)
plt.plot(x,y,'go')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bezcela funkcija')
#plt.show()

n= len(x)
y_prim = []
for i in range(n-1):
    #print i, x[i], y[i],
    delta_x = x[i+1]-x[i]
    delta_y = y[i+1]-y[i]
    #y_prim = delta_y/delta_x
    #print y_prim
    y_prim.append(delta_y/delta_x)
    #print y_prim[i]

plt.plot(x[:n-1],y_prim,'rv')

y_prim_prim = []
for i in range(n-2):
    delta_x = x[i+1]-x[i]
    delta_y_prim = y_prim[i+1]-y_prim[i]
    y_prim_prim.append(delta_y_prim/delta_x)

plt.plot(x[:-2],y_prim_prim,'b*')

y_prim2 = []
for i in range(n-2):
    delta_x = x[i]-x[i-1]
    delta_y_prim2 = y_prim[i]-y_prim[i-1]
    y_prim2.append(delta_y_prim2/delta_x)
plt.plot(x[:-2],y_prim2,'b')


plt.show()



