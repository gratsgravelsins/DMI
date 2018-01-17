# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
def mans_j1(x):
    k = 0
    a = (-1)**0*x**(2*k)/(1)
    s = a
    while k<100:
        k = k + 1
        R = (-1.) * x**2/((4*k)*(k+1))
        a = a * R
        s = s + a
    s = s * x/2
    return s
a = 1.57
b = 4.71
x = np.arange(a,b,0.01)
y = ss.j1(x)
yy = mans_j1(x)
plt.plot(x,y,'go')
plt.plot(x,yy,'b*')
plt.grid()
plt.show()

funa = mans_j1(a)
funb = mans_j1(b)
if funa * funb > 0:
    print "[%.2f,%.2f] intervālā saknes nav"%(a,b),
    print "vai ir pāru sakņu skaits"
    exit()


print "Turpinājums, ja sakne tomēr ir:"
delta_x = 1.e-3 #1.e-3 VS 0.001 vai 1*10^(-3)
k = 0
while b-a > delta_x:
    k = k + 1
    x = (a+b)/2
    funx = mans_j1(x)
    print "%3d.: a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
    if funa * funx > 0:
        a = x
    else:
        b = x


print "Gala rezultats:"
print "a=%.5f f(a)=%.5f x=%.5f"%(a,mans_j1(a),x),
print "f(x)=%.5f b=%.5f f(b)=%.5f"%(funx,b,mans_j1(b))
print "Rezultāts ir sasniegts %d iterācijas"%(k)
print "Sakne ir, kad x ir vienāds ar %.5f, tāpēc, ka y ir vienāds ar %.5f "%(x,mans_j1(x))
print "Zināms, funkcijai ir sakne, tad, kad y=0 un šajā punktā funkcija maina zīmi"
print "Nepieciešamas bija 12 iteŗācijas, jo tika izieti 12 cikli, kuros izslēdza apakšintervālus, \
kuros funkcija nemaina zīmi, līdz atlikušais intervāļs bija mazāks par %.3f. \
Ja precizitate būtu vēl lielaka, tad tiktu veiktas vairāk iterācijas un otrādi."%(delta_x)
