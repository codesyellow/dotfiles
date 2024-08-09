#!/bin/bash

dupe_script=$(ps -ef | grep "$1" | grep -v grep | wc -l | xargs)

if [ ${dupe_script} -gt 2 ]; then
  echo -e "The SCRIPT_NAME.sh script was already running!"
  exit 0
else
  nohup ~/.bin/"$1" >/dev/null 2>&1 &
fi
