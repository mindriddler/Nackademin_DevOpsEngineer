#!/bin/bash

touch name_file
echo "
Tintin
Milou
Haddock
Kalkyl
Dupond
Dupont
" > name_file

while read name_file
do
	echo ${name_file//Milou/Milou Hund}	
done < name_file > name_file2
