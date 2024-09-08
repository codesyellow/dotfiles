#/bin/bash

if [[ ! -f "/tmp/disable_server_info" ]]; then
  server_info=$(</tmp/map_display)
  output="$server_info"
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Tf2 Server Count\" }"
