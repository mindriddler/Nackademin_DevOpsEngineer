#!/bin/bash

for i in {1..10}
do
	for j in {1..10}
	do
		value=$(($i*$j))
		echo "$i * $j =" $value
	done
done
