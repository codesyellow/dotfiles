#!/bin/sh
swaybg -i ~/.wallpapers/bridge.jpg &
dunst &
nm-applet &
alsactl --file ~/.config/asound.state restore &
gammastep -O 3000 &
easyeffects --gapplication-service &
easyeffects -l LoudnessEqualizer &

