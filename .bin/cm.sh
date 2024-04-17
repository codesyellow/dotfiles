# Get the window ID using the window class
window_id=$(wmctrl -lx | grep "$1" | awk '{print $1}')

# Set the window name using xdotool
xdotool set_window --name "scratchpad" $window_id

