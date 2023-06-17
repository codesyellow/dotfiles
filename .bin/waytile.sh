#!/bin/sh

cd ~

# Tell XWayland to use a cursor theme
#export XCURSOR_THEME=GoogleDot-White

# Set a cursor size
export XCURSOR_SIZE=24
export SDL_VIDEODRIVER="wayland,x11"
export MOZ_ENABLE_WAYLAND=1
export QT_QPA_PLATFORM=wayland
exec qtile start -b wayland
