#!/bin/bash
pkill -SIGRTMIN+8 waybar
if [[ $1 = 'icon' ]]; then
  exit 1
fi

# Get the current hour (24-hour format)
current_hour=$(date +"%H")
server=$(check_server.sh)

if [[ $server == "0" ]]; then
  #  echo yes
  false
else
  if [ "$current_hour" -ge 5 ] && [ "$current_hour" -le 21 ]; then
    true
  else
    false
  fi
#  echo no
fi
