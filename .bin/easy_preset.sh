#!/bin/sh
arg=$1
file_path=~/.config/.easy_preset
if [ ! -f "$file_path" ]; then
  touch "$file_path"
  echo 'LoudnessEqualizer' >$file_path
fi

if [ -z "$1" ]; then
  current_effect=$(cat $file_path)
  if [ "LoudnessEqualizer" = "$current_effect" ]; then
    echo "eq"
    exit 1
  else
    echo "bass"
    exit 1
  fi
else
  #    flatpak run com.github.wwmm.easyeffects -l $arg
  easyeffects -l $arg
  echo $arg >$file_path
  exit 1
fi
