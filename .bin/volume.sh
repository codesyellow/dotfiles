#!/bin/bash

PIPE="/tmp/volumepipe"

start_xob() {
  # Create pipe if it doesn't exist
  [[ -p "$PIPE" ]] || mkfifo "$PIPE"

  # Check if xob pipeline is already running
  if ! pgrep -f "tail -f $PIPE" >/dev/null; then
    nohup bash -c "tail -f $PIPE | xob" >/dev/null 2>&1 &
    echo "xob started"
  fi
}

check_dependencies() {
  local missing=0
  for cmd in "$@"; do
    if ! command -v "$cmd" >/dev/null; then
      echo "Missing dependency: $cmd"
      missing=1
    fi
  done
  return $missing
}

# Check required commands
check_dependencies "xob" "pactl" "pamixer" || exit 1

# Handle volume actions
case "$1" in
up) pactl set-sink-volume @DEFAULT_SINK@ +5% ;;
up_slow) pactl set-sink-volume @DEFAULT_SINK@ +1% ;;
down) pactl set-sink-volume @DEFAULT_SINK@ -5% ;;
down_slow) pactl set-sink-volume @DEFAULT_SINK@ -1% ;;
mute) pactl set-sink-mute @DEFAULT_SINK@ toggle ;;
esac

# Fetch volume info
VOLUME=$(pamixer --get-volume)
MUTED=$(pamixer --get-mute)

# Choose icon
if [ "$MUTED" = "true" ]; then
  ICON=audio-volume-muted
elif [ "$VOLUME" -le 20 ]; then
  ICON=audio-volume-low
elif [ "$VOLUME" -le 60 ]; then
  ICON=audio-volume-medium
else
  ICON=audio-volume-high
fi

# Start xob if needed and show volume
start_xob
echo "$VOLUME" >"$PIPE"

# notify-send.sh "$VOLUME%" --replace=22 -u low -a volume -i "/usr/share/icons/AdwaitaLegacy/32x32/legacy/$ICON.png"
