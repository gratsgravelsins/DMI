# -*- coding: utf-8 -*-
# a0, a1, a2, a3
#s0 s1 s2 s3 -> S
from math import sin
x = 1. * input("LIetotaj ievadi argumentu (x): ")
print type(x) 
y = sin(x)
print "Sin(%.2f)=%.2f"%(x,y)

a0 = (-1)**0*x**1/(1)
s = a0
print "a0 = %6.2f s0 = %6.2f"%(a0,s)

a1 = (-1)**1*x**3/(1*2*3)
s =  s + a1
#s1 = s0 + a1
#s1 = a0 + a1
print "a1 = %6.2f s1 = %6.2f"%(a1,s)

a2 = (-1)**2*x**5/(1*2*3*4*5)
s = s + a2
print "a2 = %6.2f s2 = %6.2f"%(a2,s)

a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
s = s + a3
print "a3 = %6.2f s3 = %6.2f"%(a3,s)
