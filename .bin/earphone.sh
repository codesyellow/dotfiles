#!/bin/bash

audio_restored=false
notified=false
while true; do
    earphone_connected=$(cat /proc/asound/card0/codec\#0 | grep "Pin-ctls: 0x40: OUT")
    if [[ -z "$earphone_connected" ]] && [[ "$notified" == "false" ]]; then
        notify-send.sh "Earphone Connected"
        notified=true
        audio_restored=false
    elif [[ -n "$earphone_connected" ]] && [[ "$audio_restored" == "false" ]]; then
        pamixer --set-volume 30
        audio_restored=true
        notified=false
    fi
    sleep 1
done
