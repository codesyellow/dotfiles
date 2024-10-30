#!/bin/bash
if [[ -f "/tmp/gameon" ]]; then
  state="warning"
  output="<span size='15000' foreground='#4c566a'> | </span>"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"gameon\", \"class\": \"$state\"}"
