#!/usr/bin/env python3

import toml
import time
import os
from datetime import datetime

toml_file_path = "/home/cie/.config/santos_matchday.toml"

# Check if the TOML file is empty
if os.path.getsize(toml_file_path) == 0:
    print("TOML file is empty. Exiting script.")
    exit(0)

# Load the TOML file and check for required keys
try:
    with open(toml_file_path, "r") as f:
        matchday = toml.load(f)

    # Ensure required keys exist
    if 'hour' not in matchday or 'match' not in matchday:
        print("Required keys are missing in the TOML file. Exiting script.")
        exit(0)
except toml.TomlDecodeError:
    print("TOML file is malformed. Exiting script.")
    exit(0)

# Clear the TOML file content if it's not empty and has valid keys
with open(toml_file_path, "w") as f:
    pass  # This will truncate the file

MATCH_DISPLAY_TIME = 600  # 10 minutes in seconds

while True:
    match_time_str = matchday['hour']
    match = matchday['match']

    # Convert match time to a datetime object
    match_time = datetime.strptime(match_time_str, "%H:%M").time()
    current_time = datetime.now().time()
    print(match_time, current_time, MATCH_DISPLAY_TIME)

    if current_time >= match_time:
         with open("/tmp/santosmatch", "w") as f:
             pass  # Just opening the file in 'w' mode clears its content
         break
    
    with open("/tmp/santosmatch", "w") as f:
        print("time echoed")
        f.write(match_time_str)

    time.sleep(3600)  

    with open("/tmp/santosmatch", "w") as f:
        print("match echoed")
        f.write(match)

    time.sleep(MATCH_DISPLAY_TIME)
