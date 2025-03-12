#!/usr/bin/env bash

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
    classes='["warning", "cpu"]' # Use JSON array syntax
else
    classes='["normal", "cpu"]' # Use JSON array syntax
fi

text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>CPU:</span>$cpu_load%"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $cpu_load\", \"class\": $classes}"
echo $output
