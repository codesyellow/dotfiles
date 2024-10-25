#!/bin/bash

if [[ -f "/tmp/santosmatch" ]]; then
  santos=$(</tmp/santosmatch)
  output="  $santos"
  printf '<span rise="4200" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' "$output"
fi

