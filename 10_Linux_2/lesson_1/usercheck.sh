#!/bin/bash

username=$1

if [ -z "$1" ]
then
    echo "You need to provide a username. Program closing."
    exit
else
	passwd=$(grep $1 /etc/passwd)
	group=$(grep $1 /etc/group)
	if [ -n "${passwd}" ] && [ -n "${group}" ] 
	then
		echo "From passwd:"
		echo ${passwd}
		echo "--------------------------"
		echo "From group:"
		echo ${group}
 	else
 		echo "That user does not exist."
	fi
fi
