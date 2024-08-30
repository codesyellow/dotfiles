#!/bin/sh
hsetroot -cover ~/.wallpapers/ign-0011.png &
picom &
pamixer --set-volume 30 &
setxkbmap -layout "us,us" -variant ",intl" -option "grp:alt_shift_toggle,caps:ctrl_modifier,caps:escape" &
