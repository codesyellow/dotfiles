#!/bin/sh
exec_scripts.sh dwm-bar_run.sh &
setxkbmap -layout "us,us" -variant ",intl" -option "grp:alt_shift_toggle,caps:ctrl_modifier,caps:escape" &
xremap ~/.config/xremap/config.yml &
hsetroot -cover ~/.wallpapers/ign-0011.png &
#xgifwallpaper -d 12 -s FILL ~/.wallpapers/coffee-lofi.gif &
picom &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
dunst &
unclutter &
run_xidlehook &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
pamixer --set-volume 30 &
udiskie &
#xsel.sh &
systemctl --user import-environment DISPLAY &
clipmenud &
caffeine &
/usr/lib/polkit-kde-authentication-agent-1 &
sleep 5 && easyeffects --gapplication-service &
easyeffects -l 'LoudnessEqualizer' &
exec_scripts.sh music.sh &
systemctl --user start ds4_controller.service &
systemctl --user start server_check.service &
systemctl --user start server.service &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
