#!/bin/bash

# Directory to search for files
search_dir="$HOME/.mindmaps"

# Prompt user to enter a file name using dmenu
file_name=$(find "$search_dir" -maxdepth 1 -type f | sed "s|$search_dir/||" | dmenu -p "Enter file name:")

# If user pressed escape or canceled, exit
[ -z "$file_name" ] && exit

# Full path of the selected file
full_path="$search_dir/$file_name"

# Check if the file exists
if [ -e "$full_path" ]; then
    # File exists, open it with a specific software (e.g., vim)
    foot -e h-m-m "$full_path"
else
    # File does not exist, create it and then open with a specific software
    mkdir -p "$(dirname "$full_path")" # Create the directory if it doesn't exist
    touch "$full_path"
    foot -e h-m-m "$full_path"
fi
