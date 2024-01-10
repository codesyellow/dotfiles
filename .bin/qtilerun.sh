#!/bin/bash
export QT_QPA_PLATFORM=wayland
export SDL_VIDEODRIVER=wayland
export XDG_SESSION_TYPE=wayland
export XDG_CURRENT_DESKTOP=qtile 
export BEMENU_BACKEND=wayland
export MOZ_ENABLE_WAYLAND=1 
export ANKI_WAYLAND=1
export LD_BIND_NOW=1
qtile start -b wayland
