#!/bin/bash
ram_icon=
freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
memory_num=$(printf "%.0f\n" "$freemen_per")
if [[ $memory_num -ge 70 ]]; then
  output="$ram_icon $memory_num%"
  printf '<span foreground="#d8dee9">%s</span>' "$output"
fi
