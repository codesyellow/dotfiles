#!/bin/bash

# Path to your file
file="/home/cie/santos_plays"

# Loop through each line in the file
while IFS= read -r line; do
  # Process the line (e.g., print it)
  # Define the target date (MM/DD/YYYY)
  target_date=$line

  # Convert the target date to the format YYYY-MM-DD for easier comparison
  formatted_target_date=$(date -d "$target_date" +%Y-%m-%d)

  # Get the current date in the format YYYY-MM-DD
  current_date=$(date +%Y-%m-%d)

  # Convert both dates to seconds since the Unix epoch for comparison
  target_seconds=$(date -d "$formatted_target_date" +%s)
  current_seconds=$(date -d "$current_date" +%s)

  # Compare the dates
  if [ "$target_seconds" -ge "$current_seconds" ]; then
    echo "$line"
  fi
done <"$file"
