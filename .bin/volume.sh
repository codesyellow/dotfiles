#!/bin/bash
start_wob() {
    wob=$(pgrep -f "volwob")
    if [ -e "/tmp/volumepipe" ]; then
        if [ -z "$wob" ]; then
            nohup tail -f /tmp/volumepipe | wob -c ~/.config/wob/volwob.ini &
            echo "Wob wasn't running, so process was started again."
        fi
    else
        mkfifo /tmp/volumepipe 2>/dev/null
        if [ -n "$wob" ]; then
            wob_pid=$(pgrep -f "volwob")
            pkill -9 $wob_pid
            echo "killed wob"
            nohup tail -f /tmp/volumepipe | wob -c ~/.config/wob/volwob.ini &
        fi
    fi
}

case "$1" in
"up")
    pactl set-sink-volume @DEFAULT_SINK@ +5%
    ;;
"up_slow")
    pactl set-sink-volume @DEFAULT_SINK@ +1%
    ;;
"down")
    pactl set-sink-volume @DEFAULT_SINK@ -5%
    ;;
"down_slow")
    pactl set-sink-volume @DEFAULT_SINK@ -1%
    ;;
"mute")
    pactl set-sink-mute @DEFAULT_SINK@ toggle
    ;;
esac

VOLUME=$(pamixer --get-volume)
MUTE=$(echo $AMIXER | grep -o '\[off\]' | tail -n 1)
if [ "$VOLUME" -le 20 ]; then
    ICON=audio-volume-low
else
    if [ "$VOLUME" -le 60 ]; then
        ICON=audio-volume-medium
    else
        ICON=audio-volume-high
    fi
fi
if [ "$MUTE" == "[off]" ]; then
    ICON=audio-volume-muted
fi

start_wob
echo $VOLUME
echo $VOLUME >/tmp/volumepipe
pkill -RTMIN+13 waybar
#notify-send.sh $VOLUME% \
#    --replace=22 \
#    -u low \
#    -a volume \
#    -i /usr/share/icons/AdwaitaLegacy/32x32/legacy/$ICON.png
