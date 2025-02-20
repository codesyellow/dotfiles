#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
EASYEFFECTS_EQUALIZER_ICON=""
EASYEFFECTS_BASS_ICON=""
bary=$((8 * 1000))
isizea=$((12 * 1000))
easy=$(cat ~/.config/easyeffects_preset)

bar="<span size='15000' rise='$bary' foreground='$BAR_COLOR'>| </span>"
if [[ "$easy" == "HeavyBass" ]]; then
    icony=$((7 * 1000))
    isize=$((10 * 1000))
    icon="<span size='${isizea}' rise='$icony' foreground='$WARNING_COLOR'>$EASYEFFECTS_BASS_ICON</span>"
else
    icony=$((8 * 1000))
    isize=$((11 * 1000))
    icon="<span size='${isize}' rise='$icony' foreground='$NORMAL_COLOR'>$EASYEFFECTS_EQUALIZER_ICON</span>"
fi
output="{\"text\": \"$icon $bar\", \"tooltip\": \"Updates: $easy\"}"

echo $output
