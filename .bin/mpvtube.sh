#!/bin/bash

# Prompt user for YouTube URL using wofi
url=$(wofi --dmenu -p "Enter YouTube URL:")

# Check if the input is a valid YouTube URL
if [[ $url == *"youtube.com"* || $url == *"youtu.be"* ]]; then
	# Open URL in mpv
	mpv "$url"
else
	# Display an error message if the input is not a valid YouTube URL
	echo "Invalid YouTube URL"
fi
