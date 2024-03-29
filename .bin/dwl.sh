#!/bin/sh

cd ~

# Tell XWayland to use a cursor theme
#export XCURSOR_THEME=GoogleDot-White

# Set a cursor size
export XCURSOR_SIZE=24
export SDL_VIDEODRIVER=wayland
export MOZ_ENABLE_WAYLAND=1
export QT_QPA_PLATFORM=wayland
dbus-run-session dwl > ~/.cache/dwltags
