#!/bin/bash
ram_icon=
freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
memory_num=$(printf "%.0f\n" "$freemen_per")
if [[ $memory_num -ge 70 ]]; then
  output="$ram_icon $memory_num"
  printf '<span foreground="#fff">|</span> <span size="12000" foreground="#EF5A6F" rise="2500">%s</span> <span foreground="#EF5A6F" rise="2000">%s</span>' "$ram_icon" "$memory_num%"
fi
