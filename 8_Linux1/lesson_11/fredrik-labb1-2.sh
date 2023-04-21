#!/bin/bash

file=/home/$USER/.timer

if [[ $1 == "start" || $1 == "stopp" || $1 == "reset" ]]; then

	case $1 in
	start)
		if test -f "$file"; then
			sleep 0.01
		else
			echo "$file does not exist."
			echo "Creating file"
			touch $file
		fi
		if [[ $(cat $file | wc -l) != 0 ]]; then
			echo "timer is already running"
		else
			echo "Timer started at $(date +%H:%M:%S)"
			echo $(date +%H:%M:%S) >$file
		fi
		;;
	stopp)
		if [[ $(cat $file | wc -l) == 0 ]]; then
			echo "timer is not running."
		else
			echo "Stopping timer."
			echo $(date +%H:%M:%S) >>$file
			timer_started=$(head -n1 $file)
			timer_stopped=$(tail -n1 $file)
			total_seconds=$(($(date -d "$timer_stopped" +%s) - $(date -d "$timer_started" +%s)))
			hours_running=$((total_seconds / 3600))
			minutes_running=$((total_seconds % 3600 / 60))
			seconds_running=$((total_seconds % 60))
			printf "Timer ran for: %02dh:%02dm:%02ds\n" $hours_running $minutes_running $seconds_running
			rm -r $file
		fi
		;;
	reset)
		if test -f "$file"; then
			echo "Deleting file '$file'"
			rm -f $file
		else
			echo "$file does not exist."
		fi
		;;
	esac
else
	echo "Usage: $0 start|stop|reset"
	if [[ $(cat $file | wc -l) == 0 ]]; then
		sleep 0.01
	else
		echo "Timer has been running since: '$(cat $file)'"
	fi
fi
