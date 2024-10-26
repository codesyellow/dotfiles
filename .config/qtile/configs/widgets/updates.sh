#!/bin/bash

updates_num=$(checkupdates | wc -l)
if [[ $updates_num -ge 0 ]]; then
  output=" $updates_num"
  printf '<span rise="3000" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' "$output"
fi
