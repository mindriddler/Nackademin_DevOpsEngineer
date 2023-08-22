#!/bin/bash

for i in {1..10}
do
	for j in {1..10}
	do
		value=$(($i*$j))
		if [ $i == $j ]
		then
			echo "hej"
		#else
			#echo "$i * $j =" $value
		fi
	done
done
