#!/bin/sh

cputemp=$(cat /sys/class/thermal/thermal_zone2/temp | cut -c 1-2)

# Display the volume percentage
if [ "$cputemp" -ge 80 ]; then
  printf '{"text":"%s%%","class":"critical"}\n' "$cputemp"
  exit 0
elif [ "$cputemp" -ge 60 ]; then
  printf '{"text":" %s%%","class":"warning"}\n' "$cputemp"
  exit 0
elif [[ "$cputemp" -le 35 ]]; then
  printf '{"text":" %s%%","class":"low"}\n' "$cputemp"
  exit 0
else
  printf '{"text":" %s%%","class":"normal"}\n' "$cputemp"
  exit 0
fi
