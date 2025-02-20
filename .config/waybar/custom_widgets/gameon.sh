#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol=""
bary=$((8 * 1000))
icony=$((7 * 1000))
texty=$((7 * 1000))
bsize=$((15 * 1000))
tsize=$((14 * 1000))
isize=$((13 * 1000))

bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'>|</span>"
if [[ -f "/tmp/gameon" ]]; then
    icon="<span size='$isize' rise='$icony' foreground='$WARNING_COLOR'>$icon_symbol</span>"
else
    icon="<span size='$isize' rise='$icony' foreground='$NORMAL_COLOR'>$icon_symbol</span>"
fi
output="{\"text\": \"$bar $icon\", \"tooltip\": \"Updates: \"}"
echo $output
