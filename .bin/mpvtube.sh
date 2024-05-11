#!/bin/bash

# Prompt user for YouTube URL using dmenu
url=$(echo "" | dmenu -nb "#000" -z "700" -x "200" -y "2")

# Check if the input is a valid YouTube URL
if [[ $url == *"youtube.com"* || $url == *"youtu.be"* ]]; then
    # Open URL in mpv
    mpv "$url"
else
    # Display an error message if the input is not a valid YouTube URL
    echo "Invalid YouTube URL"
fi

