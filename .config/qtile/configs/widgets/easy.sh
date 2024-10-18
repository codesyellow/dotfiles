#!/bin/bash
is_easy_active=$(pgrep 'easyeffects')
if [[ -n $is_easy_active ]]; then
  easy=$(</home/digo/.config/.easy_preset)
  if [[ $easy = "LoudnessEqualizer" ]]; then
    printf '<span size="12000" foreground="#d8dee9" rise="3000"></span>'
  else
    printf '<span size="12000" foreground="#36C2CE" rise="3000"></span>'
  fi
else
  printf '<span size="12000" foreground="#ebcb8b" rise="3000">!</span>'
fi
