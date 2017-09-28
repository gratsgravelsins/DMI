#!/bin/bash

#4. piemērs
echo -e "\n"

echo "Atbilde uz jautajumu - kas tiek pildīts? "$0
#echo $n
echo "Skriptam nodoto argumentu skaits: "$#
echo "Argumentu saraksts (attēlošana/grupešana 1. veids) "$*
#ech "Argumentu saraksts (attēlošana/grupešana 2. veids) "$@
echo "Kļūdas kods(0=nav kļūdas):"$?
# 126 - comand not found
# 127 - permision denied
echo "Tekošā procesa nummurs: "$$
echo "Ēnā palaista pēdējā procesa numurs :" $!


#3. Piemēŗs
#NAME="Vārds Uzvārds"
#echo $NAME
#unset NAME
#echo $NAME

#2. Piemēŗs
#NAME="Vārds Uzvārds"
#readonly NAME
#echo $NAME
#NAME="Uzvārds Vārds"
#echo $NAME

#1. Piemēŗs
#NAME="Vārds Uzvārds"
#echo $NAME
echo -e "\n"
