# -*- coding: utf-8 -*-
a = 1. * input("Ievadi pirmo skaitli: ")
b = 1. * input("Ievadi otro skaitli: ")
c = 1. * input("Ievaid trešo skaitli: ")
if a > b and a > c and b > c:
   print ("MAX %.3f")%(a); print ("MIN %.3f")%(c); print ("Mediāna: %.3f ")%b
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(c,b,a); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(a,b,c)
elif a > b and a > c and c > b:
   print ("MAX %.3f")%(a); print ("MIN %.3f")%(b); print ("Mediāna: %.3f ")%c
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(b,c,a); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(a,c,b)
elif b > a and b > c and a > c:
   print ("MAX %.3f")%(b); print ("MIN %.3f")%(c); print ("Mediāna: %.3f ")%a
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(c,a,b); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(b,a,c)
elif b > a and b > c and c > a:
   print ("MAX %,3f")%(b); print ("MIN %.3f")%(a); print ("Mediāna: %.3f ")%c
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(a,c,b); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(b,c,a)
elif c > a and c > b and b > a:
   print ("MAX %.3f")%(c); print ("MIN %.3f")%(a); print ("Mediāna: %.3f ")%b
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(a,b,c); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(c,b,a)
elif c > a and c > b and a > b:
   print ("MAX %.3f")%(c); print ("MIN %.3f")%(b); print ("Mediāna: %.3f ")%a
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(b,a,c); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(c,a,b)
elif c > a and c > b and a == b:
   print ("MAX %.3f")%(c); print ("MIN %.3f")%(b); print ("Moda jeb vissbiežāk sastopamais skaitlis: %.3f ")%a
   print ("Mediāna: %.3f ")%a
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(b,a,c); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(c,a,b)
elif a > b and a > c and c == b:
   print ("MAX %.3f")%(a); print ("MIN %.3f")%(b); print ("Moda jeb vissbiežāk sastopamais skaitlis: %.3f ")%c
   print ("Mediāna: %.3f ")%c
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(b,c,a); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(a,c,b)
elif b > a and b > c and c == a:
   print ("MAX %.3f")%(b); print ("MIN %.3f")%(c); print ("MOda jeb vissbiežāk sastopamais skaitlis: %.3f ")%a
   print ("Mediāna: %.3f")%c
   print ("Augošā secībā: %.3f > %.3f > %.3f")%(a,c,b); print ("Dilstošā secībā: %.3f > %.3f > %.3f")%(b,c,a)
elif b == a and b == c and c == a:
   print ("MAX/MIN %.3f")%(b); print ("MOda jeb vissbiežāk sastopamais skaitlis: %.3f ")%a
   print ("Mediāna: %.3f")%c
   print ("Augošā secībā: Nav visi skaitļi vienādi!"); print ("Dilstošā secībā: Nav visi skaitļi vienādi!")

vid = (a + b + c)/3
print ("Vidējā vērtība %.5f")%vid
