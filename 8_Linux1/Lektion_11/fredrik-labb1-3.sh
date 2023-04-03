#!/bin/bash

download_file() {
	url=$1
	filename=$(basename "$url")
	curl -s -o "$filename" "$url" > /dev/null 2>&1 &
	pid=$!
	echo -n "["
	while [ -d /proc/$pid ]; do
		echo -n "#"
		sleep 0.3
	done
	echo -n "]"
}

if [[ $1 =~ "http://" || $1 =~ "https://" ]]; then
	url=$1
	download_file "$url" &
	download_pid=$!
	wait $download_pid
	filename=$(basename "$url")
	if [ -e "$filename" ]; then
	  echo -e "\nDownload complete"
	else
	  echo -e "\nDownload failed"
	fi
else
	echo "usage: $0 [URL]"
fi
