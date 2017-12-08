# -*- coding: utf-8 -*-
from math import sin
x = 1. * input("LIetotaj ievadi argumentu (x): ")
print type(x) 
y = sin(x)
print "Sin(%.2f)=%.2f"%(x,y)
a = (-1)**0*x**1/(1)
s = a
print "a0 = %6.2f s0 = %6.2f"%(a,s)

a = a * (-1) * x**2/(2*3)
s =  s + a
print "a1 = %6.2f s1 = %6.2f"%(a,s)

a = a * (-1) * x**2/(4*5)
s = s + a
print "a2 = %6.2f s2 = %6.2f"%(a,s)

a = a * (-1) * x**2 /(6*7)
s = s + a
print "a3 = %6.2f s3 = %6.2f"%(a,s)
