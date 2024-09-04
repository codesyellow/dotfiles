#!/bin/bash

updates_num=$(checkupdates | wc -l)

if [[ $updates_num -le 20 ]]; then
  state="normal"
  output=" $updates_num"
elif [[ $updates_num -ge 21 ]] && [[ $updates_num -le 40 ]]; then
  state="warning"
  output=" $updates_num"
else
  state="alert"
  output=" $updates_num"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pacman Updates\", \"class\": \"$state\"}"
