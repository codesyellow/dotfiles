#!/bin/bash

if [[ -f "/tmp/santosmatch" ]]; then
  if [[ ! -f "/tmp/stop_santos_widget" ]]; then
    santos=$(</tmp/santosmatch)
    output="  $santos"
    printf '<span rise="4200" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#4c566a">|</span>' "$output"
  fi
else
  if [[ -f "/tmp/stop_santos_widget" ]]; then
    rm "/tmp/stop_santos_widget"
  fi
fi

