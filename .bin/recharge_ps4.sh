#!/bin/bash
while true; do
    bat_stat=$(ps4_status.sh perc | sed 's/%//')
    echo $bat_stat
    if [[ $bat_stat -le '30' ]]; then
        notify-send "Battery is at $bat_stat!"                            
    fi
    echo "Dont need charge! $bat_stat"
    sleep 300
done

