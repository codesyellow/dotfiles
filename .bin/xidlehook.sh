#!/usr/bin/bash
export PRIMARY_DISPLAY="$(xrandr | awk '/ primary/{print $1}')"
#xset -dpms
xidlehook \
    `# Don't lock when there's a fullscreen application` \
    --not-when-fullscreen \
    `# Don't lock when there's audio playing` \
    --not-when-audio \
    `# Dim the screen after some minutes, undim if user becomes active` \
    --timer 150 'xrandr --output "$PRIMARY_DISPLAY" --brightness .3' \
    'xrandr --output "$PRIMARY_DISPLAY" --brightness 1' \
    `# screen off some minutes later, on & undim if user becomes active` \
    --timer 200 \
    'xset dpms force off' \
    'xset dpms force on && xrandr --output "$PRIMARY_DISPLAY" --brightness 1' \
    `# Undim & lock after some minutes` \
    --timer 600 'xrandr --output "$PRIMARY_DISPLAY" --brightness 1; slock' \
    ''#$( #\
        # Finally, suspend after it locks
    )
#--timer 180 \
#'systemctl suspend' \
#''
