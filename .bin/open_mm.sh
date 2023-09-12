#!/bin/bash

# Directory to browse
directory="/home/cie/.mindmaps/games/"

# Get a list of files in the directory
files=$(ls "$directory")

# Use dmenu to select a file
selected_file=$(echo "$files" | bemenu -p "Select a file:")

# Check if a file was selected
if [ -n "$selected_file" ]; then
    # Define the program to open the file with (e.g., h-m-m)
    program="exec.sh"
    
    echo "$program" "$directory$selected_file"

    # Open the selected file with the program
    "$program" "$selected_file" 
fi

