#!/usr/bin/env bash
notification_sended=false
while [[ true ]]; do
    whatsap=$(pgrep zapzap)

    if [[ -z "$whatsap" ]]; then
        if ! "$notification_sended"; then
            notify-send -u critical "Whatsap is not running!"
            notification_sended=true
        fi
        echo "whatsap is not running"
    else
        if "$notification_sended"; then
            notification_sended=false
            echo "notification was set to false again"
        fi
    fi
    sleep 60
done
