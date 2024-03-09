#!/bin/bash

# Specify the desired command to execute when youtube-music is running
COMMAND_TO_RUN="echo youtube-music is running (placeholder for your actual command)"

# Set the check interval (in seconds)
CHECK_INTERVAL=5

while true; do
  # Use pgrep for efficient process existence check
  if pgrep -x "Youtube Music" >/dev/null; then
    # Process is running, execute the command
    $COMMAND_TO_RUN
  fi

  # Wait for the specified interval before checking again
  sleep $CHECK_INTERVAL
done
