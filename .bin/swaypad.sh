#!/bin/bash

ddterm_id="dropdown-term"
ddterm="foot --class $ddterm_id"

sp_invisible="[app_id=$ddterm_id] opacity set 0"
sp_visible="[app_id=$ddterm_id] opacity set 1"
sp_show="[app_id=$ddterm_id] scratchpad show"
sp_resize="[app_id=$ddterm_id] resize set 100 ppt 46 ppt"
sp_move="[app_id=$ddterm_id] move position 0 ppt 52 ppt"

for ((i = 0; i < ${#1}; i++)); do
    letter="${1:$i:1}"
    case $letter in
    i) swaymsg "$sp_invisible" ;;
    v) swaymsg "$sp_visible" ;;
    s) swaymsg "$sp_show" ;;
    r)
        swaymsg "$sp_resize"
        sleep .03
        ;;
    m) swaymsg "$sp_move" ;;
    esac
done
