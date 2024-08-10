#!/bin/bash

# Download the HTML page using curl
html_content=$(curl -s "https://www.placardefutebol.com.br/time/santos/proximos-jogos")

# Extract the home team, away team, and datetime using pup
home_team=$(echo "$html_content" | pup '.match__lg_card--ht-name text{}' | xargs)
away_team=$(echo "$html_content" | pup '.match__lg_card--at-name text{}' | xargs)
datetime=$(echo "$html_content" | pup '.match__lg_card--datetime text{}' | sed 's/<br>//' | xargs)

# Format and display the match information
match_info="$home_team X $away_team, $datetime"
echo "$match_info"
