#!/bin/bash

if [[ -f "/tmp/santosmatch" ]]; then
  santos=$(</tmp/santosmatch)
  output="  $santos"
  printf '<span foreground="#EF5A6F">%s</span> <span foreground="#fff">|</span>' "$output"
fi

