#!/bin/sh
easyeffects --gapplication-service &
swaybg -i ~/.wallpapers/forest_stairs.jpg &
dunst &
nm-applet &
alsactl --file ~/.config/asound.state restore &
gammastep -O 3000 &
easyeffects -l LoudnessEqualizer &
cpupower frequency-set -g performance &
emulate_xbox.sh &
