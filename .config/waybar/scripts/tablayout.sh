#!/bin/bash

clients_icon=
clients=$(hyprctl activeworkspace | grep 'windows' | awk '{print $2}')
client_name=$(hyprctl activeworkspace | grep 'lastwindowtitle' | awk '{print $2}')
floating=$(hyprctl activewindow | grep 'floating' | awk '{print $2}')

if [[ "$floating" -ge "1" ]]; then
  ((clients--))
fi

if [[ "$clients" -le "1" ]]; then
  output=""
else
  state="warning"
  output=" $clients_icon $clients [ $client_name ] "
fi

echo "{\"text\": \"$output\", \"tooltip\": \"tablayout\", \"class\": \"$state\"}"
