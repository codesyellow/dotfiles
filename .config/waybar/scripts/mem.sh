#!/bin/bash
ram_icon=
freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
memory_num=$(printf "%.0f\n" "$freemen_per")
if [[ $memory_num -ge 70 ]]; then
  state="warning"
  output="<span size='15000' foreground='#4c566a'>| </span>$ram_icon $memory_num% "
else
  state="normal"
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
