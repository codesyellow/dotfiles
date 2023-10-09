#!/bin/bash
while true; do
  bat_stat=$(ps4_status.sh perc | sed 's/%//')
  echo $bat_stat
  if [[ -z $bat_stat ]]; then
    echo "No ps4 controller connected"
  else 
    if [[ $bat_stat -le '30' ]]; then
      notify-send "Battery is at $bat_stat!"                            
    fi
  fi
  sleep 300
done

