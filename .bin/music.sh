#!/usr/bin/env bash

# Function to handle SIGTERM
cleanup() {
  echo "SIGTERM received, cleaning up..."
  # Perform any cleanup tasks here, like saving state, releasing resources, etc.
  if [[ -f /tmp/equalizer ]]; then
    rm /tmp/equalizer
  elif [[ -f /tmp/music ]]; then
    rm /tmp/music
  fi
  exit 0
}

# Trap the SIGTERM signal and call the cleanup function
trap cleanup SIGTERM

music_preset="HeavyBass"
equalizer="LoudnessEqualizer"
music_path="/tmp/music"
equalizer_path="/tmp/equalizer"

do_exist() {
  if ! [[ -f "/tmp/$1" ]]; then
    touch "/tmp/$1"
    echo "preset was selected was $2"
    /home/cie/.bin/easy_preset.sh "$2" &
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
  effects=$(pidof 'easyeffects')

  if [[ -n "effects" ]]; then
    if [[ -n "$music" ]]; then
      do_exist "music" $music_preset
    else
      do_exist "equalizer" $equalizer
    fi
  else
    echo "easyeffects is not running. make sure its running so the script can work"
  fi
  sleep 3
done
