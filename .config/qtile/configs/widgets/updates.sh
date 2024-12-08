#!/bin/bash

updates_num=$(checkupdates | wc -l)
if [[ $updates_num -ge 20 ]]; then
  output="$updates_num"
  printf '<span size="x-large" foreground="#4c566a">| </span><span rise="3000" foreground="#EF5A6F"></span> <span rise="4300" foreground="#EF5A6F">%s</span>' "$output"
fi
