#!/bin/sh
xrandr --output VGA-1 --gamma 1.0:0.88:0.90 --brightness 0.95 &
hsetroot -cover ~/.wallpapers/rainnight.jpg &
easyeffects --gapplication-service &
xset led on &
keyd-application-mapper -d
dunst &
unclutter &
run_xidlehook &
safeeyes &
easyeffects -l 'LoudnessEqualizer' &
picom --experimental-backend &
alacritty &
