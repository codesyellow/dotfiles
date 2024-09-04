#!/bin/sh

volume=$(pamixer --get-volume)
muted=$(pamixer --get-mute)

# If the script is called with the 'icon' argument, display the icon
if [ "$1" = "icon" ]; then
  if [ "$muted" = "true" ]; then
    printf '{"text":"","class":"critical"}\n'
    exit 0
  else
    if [ "$volume" -ge 50 ]; then
      printf '{"text":"","class":"critical"}\n'
    elif [ "$volume" == 0 ]; then
      printf '{"text":"","class":"warning"}\n'
    else
      printf '{"text":"","class":"normal"}\n'
    fi
    exit 0
  fi
fi

# Display the volume percentage
if [ "$muted" = "true" ]; then
  printf '{"text":"0%%","class":"critical"}\n'
else
  if [ "$volume" -ge 50 ]; then
    printf '{"text":"%s%%","class":"critical"}\n' "$volume"
  elif [ "$volume" == 0 ]; then
    printf '{"text":"%s%%","class":"warning"}\n' "$volume"
  else
    printf '{"text":"%s%%","class":"normal"}\n' "$volume"
  fi
fi
