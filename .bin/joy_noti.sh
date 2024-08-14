#!/bin/bash
# notification_script.sh

summary="$1"
body="$2"

# Example condition: Centralize if the body contains "Important Message"
if [[ "$body" =~ "Important Message" ]]; then
  geometry="--geometry=300x50+450+20" # Adjust size and position
else
  geometry=""
fi

notify-send.sh -i ~/.local/share/icons/joystick.png "$summary" "$body" $geometry
