#!/bin/bash
while true; do
    bat_stat=$(ps4_status.sh perc | sed 's/%//')
    if [[ $bat_stat -le '30' ]]; then
        notify-send "Battery is at $bat_stat!"                            
        exit 1
    fi

    sleep 300
    echo "Dont need charge! $bat_stat"
done

