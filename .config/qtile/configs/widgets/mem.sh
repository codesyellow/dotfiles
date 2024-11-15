#!/bin/bash
ram_icon=
freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
memory_num=$(printf "%.0f\n" "$freemen_per")
if [[ $memory_num -ge 80 ]]; then
  output="$ram_icon $memory_num"
  printf '<span size="x-large" foreground="#4c566a">|</span> <span size="12000" foreground="#EF5A6F" rise="4000">%s</span> <span foreground="#EF5A6F" rise="3800">%s</span>' "$ram_icon" "$memory_num%"
fi
