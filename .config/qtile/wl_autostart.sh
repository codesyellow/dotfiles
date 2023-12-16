#!/bin/bash
swww init &
wlsunset -t 4000 &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
dunst &
flatpak run com.github.wwmm.easyeffects --gapplication-service &
wl-copy &
/usr/lib/polkit-kde-authentication-agent-1 &
wl-paste --watch cliphist store &
blueman-applet &
recharge_ps4.sh &
/usr/lib/xdg-desktop-portal-wlr &
flatpak run com.github.wwmm.easyeffects -l 'LoudnessEqualizer' &
swww img ~/.wallpapers/wall2.gif &
