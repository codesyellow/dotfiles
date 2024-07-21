#!/bin/bash
pkill -SIGRTMIN+8 waybar
if [[ $1 = 'icon' ]]; then
  exit 1
fi
# Get the current hour (24-hour format)
current_hour=$(date +"%H")

if [ "$current_hour" -ge 6 ] && [ "$current_hour" -le 22 ]; then
  true
elif [[ "$current_hour" -ge 22 ]]; then
  false
fi
