#!/usr/bin/env bash

if [ "$(cat /tmp/server_status)" = "true" ]; then
  exit 0
else
  exit 1
fi
