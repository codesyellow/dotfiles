#!/bin/bash

# Define the name of the program you want to check for
program_name=$1
new_program_name=$2

'xdotool selectwindow set_window --name "scratchpad"'
# Check if the program is running
if pgrep "$program_name" >/dev/null; then
	echo "$program_name is running."

	# Check if the program name is not what you want it to be
	if [ "$(xdotool getwindowfocus getwindowname)" != "$program_name" ]; then
		# Change the program name using xdotool
		xdotool search --name "$program_name" set_window --name "$new_program_name"
		echo "Changed $program_name to $new_program_name."
	else
		echo "$program_name is already named correctly."
	fi
else
	echo "$program_name is not running."
fi
