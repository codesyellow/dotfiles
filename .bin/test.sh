#!/bin/bash
while read -r file; do
  sudo rm -v "$file"
done <~/valid_paths.txt
