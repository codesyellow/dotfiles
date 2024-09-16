#!/bin/sh
is_running() {
  script=$(ps -ef | grep 'bash' | grep $1)
  echo "$script"
  if [[ -z "$script" ]]; then
    echo "Not running"
  else
    echo "running"
  fi
}

is_running 'pausa'


