#!/usr/bin/env bash
arandr ~/.screenlayout/restore_layout.sh &
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

#is_running 'pausa'
is_running 'easy_always.sh'
is_running 'xidlehook.sh'
is_running 'gameon.mjs' 'node'

pamixer --set-volume 30 &
picom &
#hsetroot -cover ~/.wallpapers/ign-0011.png &
nitrogen --restore &
alsactl --file ~/.config/asound.state restore &
paplay ~/.audios/retro-audio-logo-94648.mp3 &
#xrandr --output VGA-1 --gamma 1.2:1.2:1.2 &
dunst &
unclutter &
udiskie &
clipmenud &
systemctl --user import-environment DISPLAY &
/usr/lib/polkit-kde-authentication-agent-1 &
redshift -O 3000 &
xremap ~/.config/xremap/xremap &
pausa.py &
is_music.py &
