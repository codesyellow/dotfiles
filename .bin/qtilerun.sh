#!/bin/bash
QT_QPA_PLATFORM=wayland
SDL_VIDEODRIVER=wayland
XDG_SESSION_TYPE=wayland
XDG_CURRENT_DESKTOP=sway dbus-run-session qtile start -b wayland
