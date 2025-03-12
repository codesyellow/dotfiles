#!/usr/bin/env bash

total_free=$(df -BG ~/.HDD | awk 'NR==2 {print $4}' | tr -d 'G')

if [[ "$total_free" -le 10 ]]; then
    classes='["warning", "hdd"]'
else
    classes='["normal", "hdd"]'
fi

total_freeG=$(df -BG ~/.HDD | awk 'NR==2 {print $4}')
text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>HDD:</span>$total_freeG"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $total_free\", \"class\": $classes}"
echo $output
