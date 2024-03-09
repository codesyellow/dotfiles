#!/bin/sh
timer="USER INPUT"
read -p "How many minutes/seconds?: " timer

tclock timer -d $timer -e "notify-send.sh -u critical Countdown ended!!! && paplay ~/.audios/notification-sound-7062.mp3"
