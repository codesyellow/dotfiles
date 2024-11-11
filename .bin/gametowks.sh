#!/bin/bash
game=$(hyprctl activewindow | grep 'initialClass' | awk '{print $2}')
echo "windowrulev2 = workspace 7 silent,class:^($game)$" >>~/.config/hypr/configs/games-rules.conf
