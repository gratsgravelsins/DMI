# -*- coding: utf-8 -*-
k = 0
name =  raw_input("Iebadi savu vardu: ")
name1 = raw_input("Ievadi savu uzvardu: ")
print ("Tavs pilnais vārds, uzvārds ir %s %s ")%(name,name1)
gads = int(input("Ievadi savu gadu, kurā esi dzimis: "))
age = 2017 - gads
if age == 0:
  print ("Tev vēl nav gads.")
elif gads > 2017:
  print("Tu vēl neesi piedzimis!")
else:
  print ("Šogad Tev jau ir vai paliks  %d gadi.")%age
if age > 17:
  print("Tu esi pilngadīgs!")
elif age < 17 and age >= 12:
  print ("TU esi pusaudzis!")
elif age < 12 and age > 0:
  print ("Tu esi bērns!")
if age > 0: 
   print("Tu esi dzīvojis šajos gados!")
   while k <= age:
       a = 2017 - k
       k = k + 1
       print("%d")%a
apk = input("Vai velies apkopojumu?").lower()
if apk.startswith('y'):
  print("Tevi sauc %s %s, Tu esi dzimis/dzimusi %d.gadā un šogad Tev paliks vai jau ir %d gadi.")%(name,name1,gads,age)
else:
  print("TU nevēlējies apkopojumu, vai neievadīji (y vai yes vai j vai jā vai ja)")
