#!/bin/bash

# Path to status file
STATUS_FILE="/tmp/keymap_toggle_status"

# Check if the status file exists
if [ ! -f $STATUS_FILE ]; then
  touch $STATUS_FILE
  echo "wasd" >$STATUS_FILE
fi

# Read the current status
STATUS=$(cat $STATUS_FILE)

# Toggle between WASD and ESDF
if [ "$STATUS" == "wasd" ]; then
  xmodmap ~/.Xmodmap_esdf
  echo "esdf" >$STATUS_FILE
else
  xmodmap ~/.Xmodmap_wasd
  echo "wasd" >$STATUS_FILE
fi
