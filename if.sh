#!/bin/bash

#if (...) then .... elif(...) then... else... fi
a=$1
#argumenta kārtas nummurs.
if (( $a > 0 ))
then
	echo "Izdruka no galvena zara (Jā gadījumā), tad kad $a ir lielāks par 0"
elif (( $a == 0)); then
	echo "Izdr. no g. zara (Jā g.), tad, kad $a ir =0"
else
	echo "Izdr. no galv. zara (Nē gadījumā), tad, kad $a nav >0"
	echo "šis izpildas tikai, tad, kad visi iepriekšējie neizpildās"
fi










: <<'END'
#if (...) then .... fi
a=$1
#argumenta kārtas nummurs.
if (( $a > 0 ))
then
	echo "Izdruka no galvena zara (Jā gadījumā), tad kad $a ir lielāks par 0"
else
	echo "Izdr. no galv. zara (Nē gadījumā), tad, kad $a nav >0"
fi



#if (...) then .... fi
a=$1
#argumenta kārtas nummurs.
if (( $a > 0 ))
then
	echo "Izdruka no galvena zara (Jā gadījumā), tad kad $a ir lielāks par 0"
fi
echo "šis teksts tiks attēlots jebkurā gadījumā"
END

