#!/bin/sh

cpu=$(awk -v FS=" " 'NR==1 {u1=$2+$4; t1=$2+$4+$5} NR==2 {u=$2+$4; t=$2+$4+$5; printf "%.0f\n", (u-u1) * 100 / (t-t1)}' <(grep 'cpu ' /proc/stat) <(sleep 1; grep 'cpu ' /proc/stat))

# Check if the CPU usage was successfully calculated
if [ -z "$cpu" ]; then
  echo '{"text":"","class":"unknown"}'
  exit 1
fi

cpu_per_int=$(printf "%.0f\n" "$cpu")

# Display the CPU usage percentage
if [ "$cpu_per_int" -ge 90 ]; then
  printf '{"text":" %s%%","class":"critical"}\n' "$cpu_per_int"
  exit 0
elif [ "$cpu_per_int" -ge 60 ] && [ "$cpu_per_int" -le 89 ]; then
  printf '{"text":" %s%%","class":"warning"}\n' "$cpu_per_int"
  exit 0
else
  printf '{"text":" %s%%","class":"normal"}\n' "$cpu_per_int"
  exit 0
fi

