#!/bin/bash

# Find the window ID of the active window
WINDOW_ID=$(xdotool getactivewindow)

# Remove window decorations using wmctrl (alternative to xdotool for this specific task)
wmctrl -r :ACTIVE: -b add,fullscreen

# If you want to use xdotool for everything (but note that it might not remove all decorations):
# xdotool windowmove $WINDOW_ID 0 0
# xdotool windowsize $WINDOW_ID 100% 100%

# Set the window to be above other windows
xdotool windowraise $WINDOW_ID
