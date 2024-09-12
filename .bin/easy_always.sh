#!/usr/bin/env bash

easyeffects=$(pgrep 'easyeffects')

while true; do
  if [[ -z "$easyeffects" ]]; then
    nohup easyeffects --gapplication-service > output.log 2>&1 & 
  fi
  sleep 2
done

