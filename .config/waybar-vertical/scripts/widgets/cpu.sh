#!/bin/sh

cpu=$(awk -v FS=" " 'NR==1 {u1=$2+$4; t1=$2+$4+$5} NR==2 {u=$2+$4; t=$2+$4+$5; printf "%.0f\n", (u-u1) * 100 / (t-t1)}' <(grep 'cpu ' /proc/stat) <(sleep 1; grep 'cpu ' /proc/stat))

# Check if the CPU usage was successfully calculated
if [ -z "$cpu" ]; then
  echo '{"text":"","class":"unknown"}'
  exit 1
fi

cpu_per_int=$(printf "%.0f\n" "$cpu")

# If the script is called with the 'icon' argument, display the icon
if [ "$1" = "icon" ]; then
  if [ "$cpu_per_int" -ge 90 ]; then
    printf '{"text":"","class":"critical"}\n'
  elif [ "$cpu_per_int" -ge 60 ] && [ "$cpu_per_int" -le 89 ]; then
    printf '{"text":"","class":"warning"}\n'
  else
    printf '{"text":"","class":"normal"}\n'
  fi
  exit 0
fi

# Display the CPU usage percentage
if [ "$cpu_per_int" -ge 90 ]; then
  printf '{"text":"%s%%","class":"critical"}\n' "$cpu_per_int"
  pkill -RTMIN+12 waybar
  exit 0
elif [ "$cpu_per_int" -ge 60 ] && [ "$cpu_per_int" -le 89 ]; then
  printf '{"text":"%s%%","class":"warning"}\n' "$cpu_per_int"
  pkill -RTMIN+12 waybar
  exit 0
else
  printf '{"text":"%s%%","class":"normal"}\n' "$cpu_per_int"
  pkill -RTMIN+12 waybar
  exit 0
fi

