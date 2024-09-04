#!/bin/bash

if [[ -f "/tmp/climate" ]]; then
  climate_num=$(</tmp/climate)
  if [[ "$climate_num" -ge 30 ]]; then
    output=" $climate_num"
  elif [[ "$climate_num" -le 20 ]]; then
    output=" $climate_num"
  else
    output=" $climate_num"
  fi
else
  output=""
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Climate\" }"
