#!/bin/bash

# Service name to manage (replace with your actual service name)
SERVICE_NAME="keyd"

while true; do
  # Check if Steam is running
  if pgrep -f "steam" || pgrep -f "heroic" || pgrep -f "lutris"; then
    # Steam is running, check service status
    if systemctl is-active --quiet $SERVICE_NAME; then
      # Service is also running, disable it
      doas systemctl stop $SERVICE_NAME
      echo "Steam is running, disabled service $SERVICE_NAME"
    fi
  else
    # Steam is not running, check service status
    if ! systemctl is-active --quiet $SERVICE_NAME; then
      # Service is also not running, enable it
      doas systemctl start $SERVICE_NAME
      echo "Steam is not running, enabled service $SERVICE_NAME"
    fi
  fi

  # Sleep for 5 seconds before checking again
  sleep 5
done
