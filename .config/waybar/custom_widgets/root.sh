#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol="󰌪"
bary=$((8 * 1000))
icony=$((6 * 1000))
texty=$((5 * 1000))
bsize=$((14 * 1000))
tsize=$((13 * 1000))
isize=$((13 * 1000))

root_free=$(df -BG / | awk 'NR==2 {print $4}' | tr -d 'G')

if [[ "$root_free" -le 10 ]]; then
    root_freeG=$(df -BG / | awk 'NR==2 {print $4}')
    bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'> |</span>"
    icon="<span size='$isize' rise='$icony' foreground='$WARNING_COLOR'>$icon_symbol</span>"
    text="<span size='$tsize' rise='$texty' foreground='$WARNING_COLOR'>$root_freeG</span>"
    output="{\"text\": \"$bar $icon $text\", \"tooltip\": \"Updates: $root_free\"}"
    echo $output
fi
