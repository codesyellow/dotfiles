#/bin/bash

server_info=$(</tmp/map_display)
server_status="/tmp/disable_server_info"

if [[ ! -f $server_status ]]; then
  output="$server_info"
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Tf2 Server Count\" }"
