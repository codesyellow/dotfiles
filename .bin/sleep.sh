#!/bin/bash
swayidle -w timeout 300 'swaylock -i ~/.wallpapers/ign-0011.png ' \
#            timeout 600 'systemctl suspend' \
            before-sleep 'swaylock -i ~/.wallpapers/ign-0011.png' &
