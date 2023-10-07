#!/bin/bash
light-keys.sh &
swaybg -i ~/.wallpapers/house.jpg &
dunst &
flatpak run com.github.wwmm.easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
swayidle -w \
    timeout 300 'swaylock -i ~/.wallpapers/house.png' \
    before-sleep 'swaylock -i ~/.wallpapers/house.png' &
sway-audio-idle-inhibit &
swayosd-server &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
blueman-applet &
recharge_ps4.sh &
