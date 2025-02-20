#!/usr/bin/env bash

BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol="󰊴"
bary=$((8 * 1000))
icony=$((7 * 1000))
texty=$((7 * 1000))
bsize=$((15 * 1000))
tsize=$((14 * 1000))
isize=$((16 * 1000))
ds4_bat=$(dsbattery | awk '{print $2}')

bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'>| </span>"
icon="<span size='$isize' rise='$icony' foreground='$NORMAL_COLOR'>$icon_symbol</span>"
text="<span size='$tsize' rise='$texty' foreground='$NORMAL_COLOR'>$ds4_bat</span>"
if [[ -z "$ds4_bat" ]]; then
    output="{\"text\": \"$icon $bar\", \"tooltip\": \"Updates: $ds4_bat\"}"
else
    output="{\"text\": \"$icon $text $bar\", \"tooltip\": \"Updates: $ds4_bat\"}"
fi

echo $output
