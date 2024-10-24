#!/bin/bash
is_easy_active=$(pgrep 'easyeffects')
if [[ -n $is_easy_active ]]; then
  easy=$(</home/digo/.config/.easy_preset)
  if [[ $easy = "LoudnessEqualizer" ]]; then
    printf '<span size="12000" foreground="#d8dee9" rise="3000"></span>'
  else
    printf '<span size="15000" foreground="#EF5A6F" rise="5000"></span>'
  fi
else
  printf '<span size="12000" foreground="#EF5A6F" rise="3000">!</span>'
fi
