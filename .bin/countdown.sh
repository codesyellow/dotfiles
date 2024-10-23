#!/usr/bin/env bash

timer=""
seconds=""
read -p "How many minutes/seconds?: " timer 
if [[ "$timer" == *"."* ]]; then
  min="${timer%%.*}"
  sec="${timer#*.}"
  seconds=$sec
  timer=$min
elif [[ ! "$timer" =~ ^[0-9]+$ ]]; then
    notify-send "You should only pass numbers!"
    exit 1
fi
let timer=$timer*60
while true; do
  if [[ "$timer" -le 0 ]]; then
    notify-send "Time ended!"
    exit 0
  fi
  echo "$timer" > /tmp/countdown
  echo "$seconds"
  ((timer--))
  sleep 1
done

