#!/bin/bash

updates_num=$(checkupdates | wc -l)

if [[ $updates_num -ge 0 ]]; then
  state="warning"
  output=" $updates_num<span size='15000' foreground='#4c566a'> | </span>"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pacman Updates\", \"class\": \"$state\"}"
