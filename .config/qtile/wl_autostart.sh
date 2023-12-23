#!/bin/bash
paplay ~/.audios/retro-audio-logo-94648.mp3 &
swww init &
swayosd-server &
wlsunset -t 4000 &
dunst &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
blueman-applet &
recharge_ps4.sh &
/usr/lib/xdg-desktop-portal-wlr &
disable_keyd.sh &
swww img ~/.wallpapers/wall2.gif &
sleep 5 && flatpak run com.github.wwmm.easyeffects --gapplication-service &
