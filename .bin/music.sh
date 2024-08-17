#!/usr/bin/env bash

music_preset="HeavyBass"
equalizer="LoudnessEqualizer"
music_path="/tmp/music"
equalizer_path="/tmp/equalizer"

do_exist() {
  if ! [[ -f "/tmp/$1" ]]; then
    touch "/tmp/$1"
    easy_preset.sh "$2" &
  fi

  if [[ "$1" == 'music' ]]; then
    if [[ -f $equalizer_path ]]; then
      echo "Yup not music"
      rm $equalizer_path
    fi
  else
    if [[ -f $equalizer_path ]]; then
      if [[ -f $music_path ]]; then
        pamixer --set-volume 30
        rm $music_path
      fi
    fi
  fi
}

while true; do
  music=$(pidof 'youtube-music')

  if [[ -n "$music" ]]; then
    echo "running"
    do_exist "music" $music_preset
  else
    do_exist "equalizer" $equalizer
    echo "not running"
  fi

  sleep 3
done
