#!/bin/bash
is_easy_active=$(pgrep 'easyeffects')
if [[ -n $is_easy_active ]]; then
  easy=$(</home/digo/.config/.easy_preset)
  if [[ $easy = "LoudnessEqualizer" ]]; then
    printf '<span size="12000" foreground="#d8dee9" rise="4000"></span>'
  else
    printf '<span size="14500" foreground="#EF5A6F" rise="4100"></span>'
  fi
else
  printf '<span size="12000" foreground="#EF5A6F" rise="4000">!</span>'
fi
