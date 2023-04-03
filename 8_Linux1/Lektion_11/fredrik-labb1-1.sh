#!/bin/bash

while [[ $# > 0 ]]; do
	num_of_files=$(find /etc -mindepth 1 -maxdepth 1 -type f -iname $1'*' 2>/dev/null | wc -l)
	echo "Number of files in /etc starting with '$1' is: $num_of_files"
	sum=0
	for file in /etc/$1*; do
	  if [ -f "$file" ]; then
	    lines=$(wc -l < "$file")
	    echo "File $file has $lines lines."
	    ((sum += lines))
	  fi
	done
	echo -e "Total number of lines: $sum\n"
	shift
done
