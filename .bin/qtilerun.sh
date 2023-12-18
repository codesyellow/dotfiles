#!/bin/bash
export QT_QPA_PLATFORM=wayland
export SDL_VIDEODRIVER=wayland
export XDG_SESSION_TYPE=wayland
export XDG_CURRENT_DESKTOP=Hyprland 
export MOZ_ENABLE_WAYLAND=1 
export BEMENU_BACKEND=wayland
dbus-run-session qtile start -b wayland
