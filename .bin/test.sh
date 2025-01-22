#!/bin/bash

# Function to check if a game is running via Heroic
is_game_running() {
    # Get all processes launched by Heroic
    heroic_processes=$(pstree -p | grep -E "heroic-run|bwrap")

    # Check for any `.exe` processes under bwrap
    if echo "$heroic_processes" | grep -qE "\.exe"; then
        echo "A game is running via Heroic."
        return 0
    else
        echo "No game is running via Heroic."
        return 1
    fi
}

# Run the function
is_game_running
