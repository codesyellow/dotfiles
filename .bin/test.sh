#!/bin/sh
has_headphone() {
    for card in /proc/asound/card*; do
        amixer -c"${card##*card}" cget 'iface=CARD,name=Headphone Jack'
    done 2>/dev/null | grep -qw values=on
}

has_headphone
