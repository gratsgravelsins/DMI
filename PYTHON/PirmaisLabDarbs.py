# -*- coding: utf-8 -*-
#PIRMAIS LABRATORIJAS DARBS SKAITĻU TABULA AR DALĪJUMU ATLIKUMIEM!

a = input("\033[93m \033[1m Lietotāj, lūdzu ievadi skaitli: ")
k = a
print ("\033[33m \t%1 \t%2 \t%3 \t%4 \t%5 \t%10 ")
while k<=a + 10:
    k1 = k % 1
    k2 = k % 2
    k3 = k % 3
    k4 = k % 4
    k5 = k % 5
    k6 = k % 10
    print ("\033[33m%d \033[37m\t%d \033[35m\t%d \033[36m\t%d \033[32m\t%d \033[31m\t%d \033[34m\t%d  ")%(k,k1,k2,k3,k4,k5,k6)
    k = k + 1
#1)\033[xxm - krāsa, 2)\033[1m - bold 3)\t - tab atsarpe 4) % - (starp k un skaitli), lai dalījums rādītu atlikumu

