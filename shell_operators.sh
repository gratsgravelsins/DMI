#!/bin/bash

#1.piemērs

val11=`expr 2 + 2`
echo "Total value : $val11"

val12=`expr 2 + 2`
echo "Total value : $val12"

val13=`expr 2 + 2`
echo "Total value : $val13"

val14=`expr 2 + 2`
echo "Total value : $val14"

a=5
b=3
#2.piemērs - izteiksmes ar (+,-,*,/) ar konstantēm
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val33=`expr $a \* $b`
echo "a * b : $val33"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a is equal to b"
fi

if [ $a != $b ]
then
   echo "a is not equal to b"
fi

if [ $a -gt $b ]
then
	echo "$a -gt $b: a is greater than b"
else
	echo "$a -gt $b: a is not greater than b"
fi

#Cits piemērs 
val01=`expr 2 + 2`
echo "2 + 2 =: "$val01

#syntax eror šajā vietā
a=$1
b=$2

#5.piemērs
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val33=`expr $a \* $b`
echo "a * b : $val33"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"
