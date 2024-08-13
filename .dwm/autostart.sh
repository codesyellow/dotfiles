#!/bin/sh
exec_scripts.sh dwm-bar_run.sh &
exec-scripts.sh /ds4_controller.sh &
alsactl --file ~/.config/asound.state restore &
setxkbmap -layout "us,us" -variant ",intl" -option "grp:alt_shift_toggle,caps:ctrl_modifier,caps:escape" &
xremap ~/.config/xremap/config.yml &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
hsetroot -cover ~/.wallpapers/ign-0011.png &
#xgifwallpaper -d 12 -s FILL ~/.wallpapers/coffee-lofi.gif &
picom &
xrandr --output VGA-1 --gamma 1.0:0.88:0.50 --brightness 0.95 &
dunst &
unclutter &
run_xidlehook &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
#xsel.sh &
systemctl --user import-environment DISPLAY &
clipmenud &
caffeine &
/usr/lib/polkit-kde-authentication-agent-1 &
sleep 5 && easyeffects --gapplication-service &
easyeffects -l 'LoudnessEqualizer' &
exec_scripts.sh server.sh &
exec_scripts.sh server_check.sh &
