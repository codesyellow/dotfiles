#!/usr/bin/env bash

root_free=$(df -BG / | awk 'NR==2 {print $4}' | tr -d 'G')

if [[ "$root_free" -le 10 ]]; then
    classes='["warning", "root"]'
else
    classes='["normal", "root"]'
fi
root_freeG=$(df -BG / | awk 'NR==2 {print $4}')
text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>ROOT:</span>$root_freeG"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $root_freeG\", \"class\": $classes}"
echo $output
