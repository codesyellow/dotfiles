#!/usr/bin/env bash

if [[ -f "/tmp/santos" ]]; then
    BAR_COLOR="#4c566a"
    NORMAL_COLOR="#d8dee9"
    WARNING_COLOR="#EF5A6F"
    icon_symbol=""

    bary=$((4 * 1000))
    icony=$((4 * 1000))
    texty=$((3 * 1000))
    bsize=$((13 * 1000))
    tsize=$((12 * 1000))
    isize=$((12 * 1000))

    santos=$(cat /tmp/santos)
    bar="<span size='$bsize' rise='$bary' foreground='$BAR_COLOR'> | </span>"
    icon="<span size='$isize' rise='$icony' foreground='$NORMAL_COLOR'>$icon_symbol</span>"
    text="<span size='$tsize' rise='$texty' foreground='$NORMAL_COLOR'>$santos</span>"
    output="{\"text\": \"$icon $text$bar\", \"tooltip\": \"Updates: $santos\"}"
    echo $output
fi
