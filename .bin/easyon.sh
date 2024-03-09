#!/bin/bash

# Specify the program name you want to check
program_name="easyeffects"

# Use pgrep to check if the process is running
if pgrep -x "$program_name" >/dev/null
then
    printf " ON"
else
    printf " OFF"
fi
