#!/bin/sh
easyeffects --gapplication-service &
xrandr --output VGA-1 --gamma 1.0:0.88:0.90 --brightness 0.95 &
hsetroot -cover ~/.wallpapers/mountains.jpg &
xset led on &
keyd-application-mapper -d
dunst &
unclutter &
run_xidlehook &
safeeyes &
picom --experimental-backend &
nm-applet &
cpupower frequency-set -g performance &
run_xidlehook &
easyeffects -l 'LoudnessEqualizer' &
