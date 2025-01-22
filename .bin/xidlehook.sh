#!/usr/bin/bash
export PRIMARY_DISPLAY="$(xrandr | awk '/ primary/{print $1}')"
#xset -dpms
xidlehook \
    `# Don't lock when there's a fullscreen application` \
    --not-when-fullscreen \
    --not-when-audio \
    --timer 120 'redshift -oP -O 4500 -b .3' \
    'redshift -oP -O 4500 -b 1' \
    --timer 240 \
    'xset dpms force off' \
    'xset dpms force on && redshift -oP -O 4500 -b 1' \
    --timer 600 'redshift -oP -O 4500 -b 1; slock' \
    ''#$( #\
        # Finally, suspend after it locks
    )
