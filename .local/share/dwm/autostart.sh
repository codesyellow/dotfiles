#!/usr/bin/env bash
is_running() {
  if [[ "$2" == "node" ]]; then
    script=$(ps -ef | grep 'node' | grep $1)
  else
    script=$(ps -ef | grep 'bash' | grep $1)
  fi
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
is_running 'gametowks.mjs' 'node'
is_running 'santos_calendar.mjs' 'node'
is_running 'gameon.mjs' 'node'

pipewire &
pamixer --set-volume 30 &
picom &
hsetroot -cover ~/.wallpapers/ign_cityRainOther.png &
alsactl --file ~/.config/asound.state restore &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
xrandr --output VGA-1 --gamma 1.2:1.2:1.2 &
dunst &
unclutter &
udiskie &
clipmenud &
systemctl --user import-environment DISPLAY &
/usr/lib/polkit-kde-authentication-agent-1 &
redshift -O 6000 &
setxkbmap -layout "us,us" -variant ",intl" -option "grp:alt_shift_toggle,caps:ctrl_modifier,caps:escape" &
