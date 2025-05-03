#!/usr/bin/env bash

PIPE="/tmp/xobmonpipe"

# Create FIFO if it doesn't exist
[[ -p "$PIPE" ]] || mkfifo "$PIPE"

# Kill old xob monitor indicator if still running
pkill -f "tail -f $PIPE | xob"

# Start xob in background
nohup bash -c "tail -f $PIPE | xob" >/dev/null 2>&1 &

# Sleep briefly to ensure xob is ready
sleep 0.1

# Get currently focused monitor (i3wm)
focused_output=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).output')

# Map monitor name to number (customize as needed)
case "$focused_output" in
HDMI1) MON_NUM=1 ;;
VGA1) MON_NUM=2 ;;
*) MON_NUM=0 ;;
esac

# Send "monitor number" as bar value to xob
echo "$MON_NUM" >"$PIPE"
