#!/usr/bin/env bash

cpu_temp=$(cat "/sys/class/thermal/thermal_zone2/temp")
actual_temp=$(($cpu_temp / 1000))

if [[ "$actual_temp" -ge 80 ]]; then
    classes='["warning", "temp"]'
else
    classes='["normal", "temp"]'
fi
text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>TMP:</span>$actual_temp°C"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $actual_temp\", \"class\": $classes}"
echo $output
