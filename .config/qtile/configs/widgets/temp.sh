#!/bin/bash
cpu_temp_high=

cpu_temp_num=$(cut -c 1-2 </sys/class/thermal/thermal_zone2/temp)

if [[ $cpu_temp_num -ge 70 ]]; then
  output="$cpu_temp_high $cpu_temp_num°"
  printf '<span foreground="#fff">|</span> <span foreground="#EF5A6F">%s</span>' "$output"
fi
