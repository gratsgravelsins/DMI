# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
#def j1(x,n):
x = 1. * input("Lietotaj,ludzu ievadi argumentu (x): ")
y = ss.j1(x)
print "J1(%.2f)=%.2f"%(x,y)

k = 0
a = (-1)**0*x**0/(1)
s = a
print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)
while k<25:
    k = k + 1
    a = (-1) * x**2/(k*(k+1)*4)
    s = s + a
    print "a%d = %6.2f s%d = %6.2f"%(k,a,k,s)

'''
x = np.arange(0.,6.28,0.01)
f1 = j1(x,0)
plt.plot(x,f1)
plt.grid()
plt.show()
'''


