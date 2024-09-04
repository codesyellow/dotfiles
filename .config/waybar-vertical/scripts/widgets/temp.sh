#!/bin/sh

cputemp=$(cat /sys/class/thermal/thermal_zone2/temp | cut -c 1-2)

# If the script is called with the 'icon' argument, display the icon
if [ "$1" = "icon" ]; then
  if [ "$cputemp" -ge 80 ]; then
    printf '{"text":"","class":"critical"}\n'
  elif [ "$cputemp" -ge 60 ]; then
    printf '{"text":"","class":"warning"}\n'
  elif [[ "$cputemp" -le 35 ]]; then
    printf '{"text":"","class":"low"}\n'
  else
    printf '{"text":"","class":"normal"}\n'
  fi
  exit 0
fi

# Display the volume percentage
if [ "$cputemp" -ge 80 ]; then
  printf '{"text":"%s%%","class":"critical"}\n' "$cputemp"
  pkill -RTMIN+20 waybar
  exit 0
elif [ "$cputemp" -ge 60 ]; then
  printf '{"text":"%s%%","class":"warning"}\n' "$cputemp"
  pkill -RTMIN+20 waybar
  exit 0
elif [[ "$cputemp" -le 35 ]]; then
  printf '{"text":"%s%%","class":"low"}\n' "$cputemp"
  pkill -RTMIN+20 waybar
  exit 0
else
  printf '{"text":"%s%%","class":"normal"}\n' "$cputemp"
  pkill -RTMIN+20 waybar
  exit 0
fi
