#!/bin/bash

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

echo $VOLUME >/tmp/volumepipe
pkill -RTMIN+13 waybar
#notify-send.sh $VOLUME% \
#    --replace=22 \
#    -u low \
#    -a volume \
#    -i /usr/share/icons/AdwaitaLegacy/32x32/legacy/$ICON.png
