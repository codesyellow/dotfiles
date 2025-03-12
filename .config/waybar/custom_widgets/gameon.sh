#!/usr/bin/env bash

if [[ -f "/tmp/gameon" ]]; then
    icon="G-ON"
    classes='["warning", "gameon"]' # Use JSON array syntax
else
    icon="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>G-OFF</span>"
    classes='["normal", "gameon"]' # Use JSON array syntax
fi
output="{\"text\": \"$icon\", \"tooltip\": \"Updates: $pomo\", \"class\": $classes}"
echo $output
