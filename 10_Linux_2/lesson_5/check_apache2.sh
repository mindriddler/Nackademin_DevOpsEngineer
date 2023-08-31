#!/bin/bash


logfile=/home/mindriddler/Repos/Nackademin/10_Linux_2/lesson_5/check_log.log


if [ `systemctl is-active apache2` == "active" ]; then
	echo "Up" >> $logfile
else
	echo "Down" >> $logfile
fi
