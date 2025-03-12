#!/usr/bin/env bash

classes='["normal", "pomo"]' # Default classes

if [[ -f "/tmp/pomo_timer" ]]; then
    pomo=$(cat "/tmp/pomo_timer")
    classes='["warning", "pomo"]' # Use JSON array syntax

    if [[ -f "/tmp/pomo_pause" ]]; then
        text="$pomo"
    fi
else
    pomo="0:00:00"
fi

output="{\"text\": \"<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>POMO:</span>$pomo\", \"tooltip\": \"Updates: $pomo\", \"class\": $classes}"
echo "$output"
