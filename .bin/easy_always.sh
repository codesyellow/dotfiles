#!/usr/bin/env bash


while true; do
  easyeffects=$(pgrep 'easyeffects')
  if [[ -z "$easyeffects" ]]; then
    nohup easyeffects --gapplication-service > /dev/null 2>&1 & 
  fi
  sleep 1
done

