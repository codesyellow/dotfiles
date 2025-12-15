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
sxhkd &
redshift -P -O 3000 &
hsetroot -cover ~/.wallpapers/ign_unsplash32.png &
is_running 'xidlehook.sh' &
easyeffects --gapplication-service &
/usr/lib/polkit-kde-authentication-agent-1 &
systemctl --user import-environment PATH &
dunst &
clipcatd &
setxkbmap -layout us,us -variant ,intl -option caps:super -option grp:alt_shift_toggle &
caffeine &

