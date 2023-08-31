#!/bin/bash
myfile=/tmp/time_now.log
timestamp=`date +%Y-%m-%d_%H-%M-%S`

echo $timestamp ": started" >> $myfile;

while true
do
	sleep 1
done
