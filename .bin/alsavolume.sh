#!/bin/bash

while true; do
    volume=$(amixer -c 0 get 'Master' | grep -o '[0-9]*%' | head -n1 | tr -d '%')

    if [ "$volume" -lt 100 ]; then
        #        pamixer --set-volume 20
        #        amixer -c 0 set 'Master' 100%
        alsactl --file ~/.config/asound.state restore
        echo "Volume was below 100%, set to 100%."
    fi
    sleep 1
done
