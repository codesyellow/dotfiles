#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol=""
bary=$((8 * 1000))
icony=$((6 * 1000))
texty=$((5 * 1000))
bsize=$((14 * 1000))
tsize=$((13 * 1000))
isize=$((13 * 1000))
cpu_usage() {
    # Read first CPU stats
    read -r cpu user nice system idle iowait irq softirq steal guest guest_nice </proc/stat
    prev_total=$((user + nice + system + idle + iowait + irq + softirq + steal))
    prev_idle=$((idle + iowait))

    # Wait 1 second
    sleep 1

    # Read second CPU stats
    read -r cpu user nice system idle iowait irq softirq steal guest guest_nice </proc/stat
    total=$((user + nice + system + idle + iowait + irq + softirq + steal))
    idle=$((idle + iowait))

    # Calculate CPU usage
    cpu_usage=$((100 * (total - prev_total - (idle - prev_idle)) / (total - prev_total)))
    echo "$cpu_usage"
}

cpu_load=$(cpu_usage)

if [[ "$cpu_load" -ge 80 ]]; then
    bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'> |</span>"
    icon="<span size='$isize' rise='$icony' foreground='$WARNING_COLOR'>$icon_symbol</span>"
    text="<span size='$tsize' rise='$texty' foreground='$WARNING_COLOR'>$cpu_load%</span>"
    output="{\"text\": \"$bar $icon $text\", \"tooltip\": \"Updates: $cpu_load\"}"
    echo $output
fi
