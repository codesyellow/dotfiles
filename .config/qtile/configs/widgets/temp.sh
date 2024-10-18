#!/bin/bash
cpu_temp_high=

cpu_temp_num=$(cut -c 1-2 </sys/class/thermal/thermal_zone2/temp)

if [[ $cpu_temp_num -ge 60 ]]; then
  output="$cpu_temp_high $cpu_temp_num°"
  printf '<span foreground="#36C2CE">%s</span>' "$output"
fi
