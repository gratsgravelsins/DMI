# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
def mans_j1(x):
    y = ss.j1(x)
    return y
N = 100000
x = []
y = []
a = 0.
b = np.pi
c = -4.
d = 4.
for i in range(N):
    x.append(random.uniform(a,b))
    #print "Kā veidojās x masīvs: ",x
for i in range(N):
    y.append(random.uniform(c,d))
    #print "Kā veidojās y masīvs: ",y

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_j1(x[i]) and y[i] > 0) \
    or (y[i] > mans_j1(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()
plt.show()

areaRect = (b-a)*(d-c)
areaFunc = areaRect * len(green_x) / N
print areaFunc
print "Laukums starp funkcijas un x asi, kas ir aizkrāsots ar zaļo krāsu vienāds \
ar %.3f intervālā no %.2f līdz %.2f"%(areaFunc,a,b)
#print "Kods darbojas - 1. Importēju visas nepieciešamās bibliotēkas \
#2. Nodefinēju savu funk. 3. Skriptam iedodu punktu skaitu N=%d \
#4. nosakam intervalu robežas 5. Liekam izvēlies nejauši skaitļus šajā intervālā \
#6. aprēķinam y un ja y ir starp funk un x asi, tad punktu nokrāsojam zaļu, ja nav tad sarkanu \
#7. attēlojam visu grafikā"%(N)
print "Koda jēga ir atrast laukumu pēc Monte Karlo metodes. Pēc šīs metodes \
punkti tiek nejauši izvēlētie mūsu noteiktajā laukumā. Ņemot ļoti daudz \
punktus, tie homogēni sadalās pa visu laukumu. Punkti starp funk un x asi \
tie iekrāsoti zaļi, bet pārējie sarkani. Laukums tiek aprēķināts \
viss laukums(tainstūris(vienkārša forma)) reizināts ar zaļo punktu \
skaita attiecību pret visiem punktiem. "
