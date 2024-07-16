#!/bin/bash

# URL of the web page
URL="https://teamwork.tf/community/quickplay/class-wars"

# Fetch the web page content with a User-Agent header
content=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" "$URL")

# Extract the specific server block
server_block=$(echo "$content" | grep -oP '(?s)PG \| CLASS WARS US \| DUSTBOWL \| RTD ████.*?server-playerInfo">[^<]*')

# Extract the player count from the specific server block
result=$(echo "$server_block" | grep -oP '[0-9]+ / [0-9]+ players')

# Print the result
if [[ -n "$result" ]]; then
  echo "Found: $result"
else
  echo "Pattern not found"
fi
