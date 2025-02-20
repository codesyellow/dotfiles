#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol=""
bary=$((8 * 1000))
icony=$((6 * 1000))
texty=$((5 * 1000))
bsize=$((14 * 1000))
tsize=$((13 * 1000))
isize=$((13 * 1000))

mem_usage=$(awk '/MemTotal/ {total=$2} /MemAvailable/ {available=$2} END {printf("%.0f\n", (total-available)/total * 100)}' /proc/meminfo)

if [[ "$mem_usage" -ge 90 ]]; then
    bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'> |</span>"
    icon="<span size='$isize' rise='$icony' foreground='$WARNING_COLOR'>$icon_symbol</span>"
    text="<span size='$tsize' rise='$texty' foreground='$WARNING_COLOR'>$mem_usage%</span>"
    output="{\"text\": \"$bar $icon $text\", \"tooltip\": \"Updates: $mem_usage\"}"
    echo $output
fi
