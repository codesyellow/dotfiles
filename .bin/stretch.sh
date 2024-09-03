#!/usr/bin/env bash

times=0
seconds=0
wait=0
stretch_path="/tmp/stretch"

display_help() {
  echo "options:
  -h, --help  show this help message and exit
  -t       How many times you want the to stretch
  -s       How many seconds you want for each stretch
  -w       How many seconds you want to stop between each stretch"
}

# Parse command-line options
while getopts ":t:s:w:h" opt; do
  case ${opt} in
  t)
    times=$OPTARG
    ;;
  s)
    seconds=$OPTARG
    ;;
  w)
    wait=$OPTARG
    ;;
  h)
    display_help
    exit 0
    ;;
  \?)
    echo "Invalid option: -$OPTARG" >&2
    display_help
    exit 1
    ;;
  :)
    echo "Option -$OPTARG requires an argument." >&2
    display_help
    exit 1
    ;;
  esac
done

if [[ "$@" == "" ]]; then
  display_help
  exit 1
fi

while [[ "$times" -ge 0 ]]; do
  if [[ "$times" == 0 ]]; then
    paplay ~/.audios/stretch_ended.wav
    break
    notify-send -u critical "Stretch ended!"
  else
    paplay ~/.audios/stretch_start.wav
    sleep $seconds
    if [[ -n "$wait" ]] && [[ ! "$times" == 1 ]]; then
      echo "Stop!!"
      paplay ~/.audios/stretch_breaks.mp3
      sleep $wait
    fi
  fi

  ((times--))
done
