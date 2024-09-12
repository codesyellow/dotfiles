#!/bin/bash

# Prompt user for YouTube URL using dmenu
url=$(echo "" | dmenu -nb "#2e3440" -z "497" -x "200" -y "1" -sb "#2e3440" -shb "#2e3440" -fn "JetBrainMono Nerd Font:size=12" -p "")

# Check if the input is a valid YouTube URL
if [[ $url == *"youtube.com"* || $url == *"youtu.be"* ]]; then
  # Open URL in mpv
  mpv "$url"
else
  # Display an error message if the input is not a valid YouTube URL
  echo "Invalid YouTube URL"
fi
