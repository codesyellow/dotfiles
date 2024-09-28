#!/bin/bash

# Fetch all clients (windows) from Hyprland
clients=$(hyprctl clients -j)

# Loop through each workspace
for workspace in $(echo "$clients" | jq -r '.[].workspace.id' | sort -u); do
  echo "Workspace $workspace:"

  # Loop through each client (window) in the current workspace
  echo "$clients" | jq --arg workspace "$workspace" -r '.[] | select(.workspace.id == ($workspace | tonumber)) | "Window: \(.title), Class: \(.class)"'

  echo "--------------------------------------"
done
