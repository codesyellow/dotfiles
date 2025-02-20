#!/usr/bin/env bash
BAR_COLOR="#4c566a"
NORMAL_COLOR="#d8dee9"
WARNING_COLOR="#EF5A6F"
icon_symbol=""
bary=$((8 * 1000))
icony=$((8 * 1000))
texty=$((7 * 1000))
bsize=$((15 * 1000))
tsize=$((12 * 1000))
isize=$((11 * 1000))
bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'> |</span>"
icon="<span size='$isize' rise='$icony' foreground='$NORMAL_COLOR'>$icon_symbol</span>"

if [[ -f "/tmp/countdown_timer" ]]; then
    pomo=$(cat "/tmp/countdown_timer")
    bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'>| </span>"
    icon="<span size='$isize' rise='$icony' foreground='$NORMAL_COLOR'>$icon_symbol</span>"
    text="<span size='$tsize' rise='$texty' foreground='$NORMAL_COLOR'>$pomo</span>"
    output="{\"text\": \"$icon $text $bar\", \"tooltip\": \"Updates: $pomo\"}"

    echo $output
fi
