#!/bin/bash
cpu_temp_high=

cpu_temp_num=$(cut -c 1-2 </sys/class/thermal/thermal_zone2/temp)

if [[ $cpu_temp_num -ge 70 ]]; then
  state="warning"
  output="<span size='15000' foreground='#4c566a'>| </span>$cpu_temp_high $cpu_temp_num° "
else
  state="normal"
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"temperature\", \"class\": \"$state\"}"
