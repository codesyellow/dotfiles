#!/bin/bash
sleep 3
# Define a variable to store the value
value=0

# Function to display usage information
usage() {
    echo "Usage: $0 <increment>"
    echo "Example: $0 10"
}

# Check if an argument is provided
if [ $# -ne 1 ]; then
    usage
    exit 1
fi

# Loop for 10 seconds
for ((i=0; i<10; i++)); do
    # Increment the value by the argument passed
    value=$((value + $1))
    ydotool mousemove -x $value  -y 0
    echo "Current value: $value"
    sleep 1  # Adjust the sleep duration as needed
done

echo "Script finished."

