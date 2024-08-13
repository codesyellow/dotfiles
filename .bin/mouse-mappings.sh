#!/bin/bash

while true; do
  xb_isrunning=$(pgrep xbindkeys)
  game=$1
  game_isrunning=$(pidof -x $1)

  if [[ -n "$game_isrunning" ]]; then
    if [[ -z "$xb_isrunning" ]]; then
      nohup xbindkeys 2>&1 &
    fi
  else
    if [[ -n "$xb_isrunning" ]]; then
      echo "the game is not running but xbind is"
      killall xbindkeys && echo "xbindkeys killed!"
    else
      echo "no x"
      echo "neither the game or xbind is running"
    fi
  fi

  sleep 5
done
