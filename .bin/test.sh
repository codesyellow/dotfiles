#!/bin/bash
root_free=$(df -BG / | awk 'NR==2 {print $4}' | tr -d 'G')
home_free=$(df -BG /home | awk 'NR==2 {print $4}' | tr -d 'G')
hdd_free=$(df -BG ~/.HDD | awk 'NR==2 {print $4}' | tr -d 'G') # Change if needed

echo "Root Free: ${root_free}G"
echo "Home Free: ${home_free}G"
echo "HDD Free: ${hdd_free}G"
