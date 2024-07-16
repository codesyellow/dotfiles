#!/bin/bash

# Program to check output
CHECK_PROGRAM="dsbattery"

# Program to kill
KILL_PROGRAM="xboxdrv"

# Function to check if the program to kill is running
is_program_running() {
	pgrep "$KILL_PROGRAM" >/dev/null 2>&1
}

# Main loop
while true; do
	# Run the check program and capture its output
	OUTPUT=$($CHECK_PROGRAM)

	if [ -z "$OUTPUT" ]; then
		# Check if the program to kill is running
		if [[ -z is_program_running ]]; then
			pkill "$KILL_PROGRAM"
			echo "Killed $KILL_PROGRAM because $CHECK_PROGRAM output was empty."
		fi
	else
		if [ ! is_program_running ]; then
			echo 'oi'
			nohup emulate_xbox_ps4.sh &
		fi
	fi

	# Wait for 1 minute
	sleep 5
done
