#!/usr/bin/env bash

LOCK_FILE="/tmp/temp_alert.lock"

if [[ -f "$LOCK_FILE" ]]; then
    exit 0
fi

GPU_LIMIT_IDLE=80
GPU_LIMIT_GAMING=90
CPU_LIMIT_IDLE=80
CPU_LIMIT_GAMING=90
IS_GAMING_PERC=80

GPU_USAGE=$(cat /sys/class/drm/card1/device/gpu_busy_percent 2>/dev/null)
GPU_TEMP_RAW=$(cat /sys/class/drm/card1/device/hwmon/hwmon*/temp1_input 2>/dev/null | head -n1)
GPU_TEMP=$((GPU_TEMP_RAW / 1000))
CPU_TEMP=$(sensors | awk '/Package id 0:/ {print int($4)}' | tr -d '+°C')

im_gaming=false
if [[ "$GPU_USAGE" -ge "$IS_GAMING_PERC" ]]; then
    im_gaming=true
fi


notify() {
    notify-send -u critical "$1"
}

should_notify() {
    local temp=$1
    local name=$2

    if $im_gaming; then
        limit=90
    else
        limit=80
    fi

    if [[ "$temp" -ge "$limit" ]]; then
        notify "$name temperature is too high: ${temp}°C"
        touch "$LOCK_FILE"
        sleep 300
        rm "$LOCK_FILE"
    fi
}

should_notify "$CPU_TEMP" "CPU"
should_notify "$GPU_TEMP" "GPU"
