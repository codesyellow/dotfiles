#!/usr/bin/env bash
is_running() {
  script=$(ps -ef | grep 'bash' | grep $1)
  echo "$script"
  if [[ -z "$script" ]]; then
    $1 &
  fi
}

is_running 'pausa'
is_running 'dwm-bar.sh'
is_running 'easy_always.sh'
is_running 'tf2_server_count.sh'
is_running 'santos_pregame.sh'
is_running 'xidlehook.sh'

pamixer --set-volume 30 &
picom &
hsetroot -cover ~/.wallpapers/ign-0011.png &
alsactl --file ~/.config/asound.state restore &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
xrandr --output VGA-1 --gamma 1.2:1.2:1.2 &
dunst &
unclutter &
#dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &
udiskie &
#systemctl --user import-environment DISPLAY &
clipmenud &
/usr/lib/polkit-kde-authentication-agent-1 &
redshift -O 6000 &
setxkbmap -layout "us,us" -variant ",intl" -option "grp:alt_shift_toggle,caps:ctrl_modifier,caps:escape" &
