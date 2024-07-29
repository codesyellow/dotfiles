#!/bin/sh

volume=$(pamixer --get-volume)
muted=$(pamixer --get-mute)

# Display the volume percentage
if [ "$muted" = "true" ]; then
  printf '{"text":" 0%%","class":"critical"}\n'
else
  if [ "$volume" -ge 50 ]; then
    printf '{"text":" %s%%","class":"critical"}\n' "$volume"
  elif [ "$volume" == 0 ]; then
    printf '{"text":" %s%%","class":"warning"}\n' "$volume"
  else
    printf '{"text":" %s%%","class":"normal"}\n' "$volume"
  fi
fi
