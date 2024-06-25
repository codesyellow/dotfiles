#!/bin/sh
paplay ~/.audios/retro-audio-logo-94648.mp3 &
#hsetroot -cover ~/.wallpapers/forest_stairs.jpg &
xgifwallpaper -d 3 -s FILL ~/.wallpapers/train-station.gif &
picom --animations -b &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
#easyeffects --gapplication-service &
dunst &
unclutter &
run_xidlehook &
#easyeffects -l 'LoudnessEqualizer' &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
xsel.sh &
systemctl --user import-environment DISPLAY &
clipmenud &
caffeine &
/usr/lib/polkit-kde-authentication-agent-1 &
blueman-applet &
flatpak run com.github.eneshecan.WhatsAppForLinux &
sleep 5 && flatpak run com.github.wwmm.easyeffects --gapplication-service &
flatpak run com.github.wwmm.easyeffects -l 'LoudnessEqualizer' &
setxkbmap -layout "us,us" -variant ",intl" -option "grp:alt_space_toggle,caps:ctrl_modifier,caps:escape" &
