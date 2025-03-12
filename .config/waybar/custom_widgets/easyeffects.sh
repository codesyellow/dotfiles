#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
EASYEFFECTS_EQUALIZER_ICON=""
EASYEFFECTS_BASS_ICON=""
bary=$((8 * 1000))
isizea=$((12 * 1000))
easy=$(cat ~/.config/easyeffects_preset)

if [[ "$easy" == "HeavyBass" ]]; then
    classes='["warning", "easy"]' # Use JSON array syntax
    icon="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>FX:</span>MUS"
else
    classes='["normal", "easy"]' # Use JSON array syntax
    icon="<span font_family='VictorMono Nerd Font Mono' font_weight='ultralight'>FX:</span>EQ"
fi
output="{\"text\": \"$icon\", \"tooltip\": \"Updates: $easy\", \"class\": $classes}"

echo $output
