# -*- coding: utf-8 -*-
#OTRAIS LABRATORIJAS DARBS GRATS GRAVELSINS REBC04
import scipy.special as ss #importēju, zem segvārda "ss" var izmantot jebkādu
import matplotlib.pyplot as plt
import numpy as np
print "               1000"
print "             -------- "
print "              \                       2k"
print "         X     \          (-1)   *   X "
print "j1(x) = --- *   |     = -----------------------------  "
print "         2     /                          2k   "
print "              /          k! * (k + 1)! * 2  "
print "             --------     "
print "              k = 0 "
print ("\n   \t\t    \t     2\n   \t\t(-1)   *   x  \t\n  R    = -----------------------------\t\n   \t    (4  *  k) * (k + 1) \t\n  \t\n")
def mans_j1(x):
    k = 0
    a = (-1)**0*x**(2*k)/(1)
    s = a
    print ("Pirmais saskātāmais: a%d = %.2f")%(k,a)
    while k<500:
        k = k + 1
        R = (-1.) * x**2/((4*k)*(k+1))
        a = a * R
        s = s + a
        if k >=499:
            print ("a%g = %e ")%(k,a)
    s = s * x/2
    return s
#x = 1. * input("Ievadi argumenta vērtību (x): ")
x = np.float128(input("Ievadi argumenta vērtību (x): "))
y = ss.j1(float(x))
print "Standarta J1(%.2f)=%.3f"%(x,y)
n = mans_j1(x)
print ("mans_j1(%.2f)=%.3f")%(x,n)

