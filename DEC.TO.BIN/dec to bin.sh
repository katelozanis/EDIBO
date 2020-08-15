#!/bin/bash

#if [ $# -eq 0 ]; then
#	echo "No argument provided. Exiting."
#	exit
#elif [ $# -gt 1 ]; then
#	echo "More than 1 argument provided. Exiting."
#	exit
#fi
#REGEXP="^[0-9]+$"
#if ! [[ $1 =~ $REGEXP  ]]; then 
#	echo "Argument NaN. Exiting."
#	exit
#fi

#DEC_VAL=$1

echo "Please provide a decimal value you wish to convert to binary:"
read DEC_VAL

DIV_RES=$DEC_VAL
BIN_DIGITS=()
COUNTER=0

while [ $DIV_RES -ge 2 ]; do
	BIN_DIGITS[$COUNTER]=$(($DIV_RES%2))
	DIV_RES=$(($DIV_RES/2))
	COUNTER=$(($COUNTER+1))
	#echo $COUNTER
done

BIN_DIGITS[$COUNTER]=$(($DIV_RES))
#echo ${BIN_DIGITS[*]}
ARR_POS=${#BIN_DIGITS[@]}
#echo $ARR_POS

BIN_VAL=""
while [ $ARR_POS -ge 0 ]; do
	BIN_VAL=$BIN_VAL${BIN_DIGITS[$ARR_POS]}
	ARR_POS=$(($ARR_POS-1))
done

echo -e "$DEC_VAL converted to binary equals:\n$BIN_VAL"
