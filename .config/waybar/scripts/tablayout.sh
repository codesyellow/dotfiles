#!/bin/bash

clients_icon=
clients=$(hyprctl activeworkspace | grep 'windows' | awk '{print $2}')
client_name=$(hyprctl activeworkspace | awk '/lastwindowtitle/ {print $2; exit}')
steamNotification=$(hyprctl clients | grep initialTitle | grep 'notificationtoasts_' | wc -l)
steamMenu=$(hyprctl clients | grep -A 1 "initialClass: steam" | grep -c 'initialTitle')
IsSteamMenu=$(hyprctl clients | grep -A 1 "initialClass: steam"  | grep 'initialTitle:' | grep -c "Steam")

if [[ $steamMenu -ge 2 ]] && [[ $IsSteamMenu == 1 ]]; then
  let clients-=1
fi

if [[ -z "$client_name" ]]; then
  let clients-=1
fi

if [[ "$steamNotification" > 0 ]]; then
  let clients-=steamNotification
fi

if [[ "$clients" -ge "2" ]]; then
  state="warning"
  output="$clients_icon $clients<span size='15000' foreground='#4c566a'> | </span>"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"tablayout\", \"class\": \"$state\"}"
