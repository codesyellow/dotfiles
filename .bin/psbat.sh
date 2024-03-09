#!/bin/bash

text=$(dsbattery)
result=$(echo "$text" | grep -o '[0-9]*%')
if [[ -z "$result" ]]; then
  printf '󰊵'
else
  printf '%s' "󰨢 $result"
fi

