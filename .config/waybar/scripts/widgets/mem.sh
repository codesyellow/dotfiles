#!/bin/sh

freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
freemen_per_int=$(printf "%.0f\n" "$freemen_per")

# If the script is called with the 'icon' argument, display the icon
if [ "$1" = "icon" ]; then
  if [ "$freemen_per_int" -ge 80 ]; then
    printf '{"text":"","class":"critical"}\n'
  elif [ "$freemen_per_int" -ge 60 ] && [ "$freemen_per_int" -le 89 ]; then
    printf '{"text":"","class":"warning"}\n'
  else
    printf '{"text":"","class":"normal"}\n'
  fi
  exit 0
fi

# Display the CPU usage percentage
if [ "$freemen_per_int" -ge 90 ]; then
  printf '{"text":"%s%%","class":"critical"}\n' "$freemen_per_int"
elif [ "$freemen_per_int" -ge 60 ] && [ "$freemen_per_int" -le 89 ]; then
  printf '{"text":"%s%%","class":"warning"}\n' "$freemen_per_int"
else
  printf '{"text":"%s%%","class":"normal"}\n' "$freemen_per_int"
fi
