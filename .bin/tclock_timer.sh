#!/bin/sh
timer="USER INPUT"
read -p "How many minutes/seconds?: " timer

tclock -c Yellow timer -d $timer -e "notify-send.sh -u critical Countdown ended!!! && paplay ~/.audios/system-notification-199277.mp3; sleep 4 && killall tclock"
