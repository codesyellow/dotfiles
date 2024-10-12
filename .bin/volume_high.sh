#!/usr/bin/env bash

while true; do
    volume=$(pamixer --get-volume)
    if [[ "$volume" -ge 50 ]] && [[ -f "/tmp/gameon" ]]; then
        pamixer --set-volume 30
        echo "foi"
    fi
    sleep 1
done
