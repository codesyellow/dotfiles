#!/bin/bash

# Use curl and pup to get the player count
player_count=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" https://www.battlemetrics.com/servers/tf2/16583539 | pup 'dt:contains("Player count") + dd text{}')

# Split the player count into two variables
current_players=$(echo $player_count | cut -d'/' -f1)
max_players=$(echo $player_count | cut -d'/' -f2)

# Output the values (or use them as needed)
echo "Current Players: $current_players"
echo "Max Players: $max_players"
