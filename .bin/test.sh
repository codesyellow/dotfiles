#!/bin/bash
sleep 3
steamMenu=$(hyprctl clients | grep -A 1 "initialClass: steam"  | grep 'initialTitle:')

if [[ $steamMenu != *"initialTitle: ''"* ]]; then
  echo "true"
fi
echo $steamMenu
