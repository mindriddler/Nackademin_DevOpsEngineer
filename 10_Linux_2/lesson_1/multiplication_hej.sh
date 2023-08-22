#!/bin/bash

for i in {1..10}
do
	echo $i"ans tabell"
	for j in {1..10}
	do
		value=$(($i*$j))
		if [ $i == $j ]
		then
			echo "hej ($i * $j)"
		else
			echo "$i * $j =" $value
		fi
	done
	echo ""
done
