#!/bin/bash

username=$1

if [ -z "$1" ]
then
        echo "You need to provide a username. Program closing."
        exit
fi

echo "From passwd:"
cat /etc/passwd | grep "$username"
echo "-------------------------------------"
echo "From group:"
cat /etc/group | grep "$username"
