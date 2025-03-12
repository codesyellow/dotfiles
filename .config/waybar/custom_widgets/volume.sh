#!/usr/bin/env bash

volume=$(pamixer --get-volume)

if [[ "$volume" -ge 50 ]]; then
    classes='["warning", "volume"]' # Use JSON array syntax
else
    classes='["normal", "volume"]' # Use JSON array syntax
fi
text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>VOL:</span>$volume%"
output="{\"text\": \"$text\", \"tooltip\": \"Updates: $volume\", \"class\": $classes}"
echo $output
