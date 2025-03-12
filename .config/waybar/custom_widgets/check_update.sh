#!/usr/bin/env bash

updates=$(checkupdates | wc -l)

text="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>UP:</span>$updates"

if [[ $updates -ge 20 ]]; then
    classes='["warning", "ram"]' # Use JSON array syntax
else
    classes='["normal", "ram"]' # Use JSON array syntax
fi

output="{\"text\": \"$text\", \"tooltip\": \"Updates: $updates\", \"class\": $classes}"
echo $output
