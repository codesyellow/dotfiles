#!/bin/sh
swaybg -m center -i ~/.wallpapers/forest_stairs.jpg &
dunst &
nm-applet &
alsactl --file ~/.config/asound.state restore &
gammastep -O 4000 &
easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

