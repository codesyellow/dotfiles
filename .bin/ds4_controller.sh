#!/usr/bin/env bash

# Notification for battery level below 50%
ds4_bat_warnings_50() {
  if [[ $1 -le 50 ]]; then
    if ! [[ -f /tmp/fwarning_50 ]]; then
      notify-send.sh -i ~/.local/share/icons/joystick.png "Battery below 50% - Plug me in!"
      touch /tmp/fwarning_50
    fi
  else
    if [[ -f /tmp/fwarning_50 ]]; then
      rm /tmp/fwarning_50
    fi
  fi
}

# Notification for battery level below 30%
ds4_bat_warnings_30() {
  if [[ $1 -le 30 ]]; then
    if ! [[ -f /tmp/fwarning_30 ]]; then
      notify-send.sh -i ~/.local/share/icons/joystick.png "Battery critically low - Plug me in immediately!"
      touch /tmp/fwarning_30
    fi
  else
    if [[ -f /tmp/fwarning_30 ]]; then
      rm /tmp/fwarning_30
    fi
  fi
}

# Notification for the first time the DS4 is connected
ds4_first_connected() {
  if ! [[ -f /tmp/ds4_first_connect ]]; then
    notify-send.sh -i ~/.local/share/icons/joystick.png "DS4 was connected!"
    touch /tmp/ds4_first_connect
  fi
}

# Main function to check battery level and handle notifications
ds4() {
  if [[ -z "$1" ]]; then
    echo "false" >/tmp/ds4_status
    rm /tmp/ds4_first_connect
  else
    echo "true" >/tmp/ds4_status
    echo "$1" >/tmp/ds4_battery
    ds4_first_connected
    ds4_bat_warnings_50 $1
    ds4_bat_warnings_30 $1
  fi
}

# Loop to continuously check the battery level
while true; do
  text=$(dsbattery)
  result=$(echo "$text" | grep -o '[0-9]*')
  ds4 $result
  sleep 30
done
