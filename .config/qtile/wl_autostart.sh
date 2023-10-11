#!/bin/bash
light-keys.sh &
swaybg -i ~/.wallpapers/house.jpg &
dunst &
easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
swayidle -w \
    timeout 300 'swaylock -i ~/.wallpapers/house.jpg' \
    before-sleep 'swaylock -i ~/.wallpapers/house.jpg' &
sway-audio-idle-inhibit &
swayosd-server &
blueman-applet &
easyeffects -l 'LoudnessEqualizer' &
recharge_ps4.sh &
/usr/lib/xdg-desktop-portal-wlr &
