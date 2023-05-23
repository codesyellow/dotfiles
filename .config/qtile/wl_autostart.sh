#!/bin/sh
swaybg -m center -i ~/.wallpapers/bridge.jpg &
dunst &
nm-applet &
alsactl --file ~/.config/asound.state restore &
gammastep -O 4000 &
easyeffects --gapplication-service &
wl-copy &
