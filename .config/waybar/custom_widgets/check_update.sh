#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol="󰇚"
bary=$((8 * 1000))
icony=$((8 * 1000))
texty=$((8 * 1000))
updates=$(checkupdates | wc -l)

bar="<span size='15000' rise='$bary' foreground='$BAR_COLOR'>| </span>"
icon="<span size='14000' rise='$icony' foreground='$WARNING_COLOR'>$icon_symbol</span>"
text="<span size='12000' rise='$texty' foreground='$WARNING_COLOR'>$updates</span>"
output="{\"text\": \"$icon $text $bar\", \"tooltip\": \"Updates: $updates\"}"

if [[ $updates -ge 20 ]]; then
    echo $output
fi
