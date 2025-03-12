#!/usr/bin/env bash

mem_usage=$(awk '/MemTotal/ {total=$2} /MemAvailable/ {available=$2} END {printf("%.0f\n", (total-available)/total * 100)}' /proc/meminfo)

if [[ "$mem_usage" -ge 80 ]]; then
    classes='["warning", "ram"]' # Use JSON array syntax
else
    classes='["normal", "ram"]' # Use JSON array syntax
fi
text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>RAM:</span>$mem_usage%"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $mem_usage\", \"class\": $classes}"
echo $output
