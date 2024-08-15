#!/bin/bash
battery_status=$(dsbattery)

# Check if the output contains the charging symbol "↑"
if [[ "$battery_status" == *"↑"* ]]; then
  echo "Controller is charging"
else
  echo "Controller is not charging"
fi
