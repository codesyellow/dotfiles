#!/bin/bash

updates_num=$(checkupdates | wc -l)
if [[ $updates_num -ge 20 ]]; then
  output=" $updates_num"
  printf '<span foreground="#EF5A6F">%s</span> <span foreground="#fff">|</span>' "$output"
fi
