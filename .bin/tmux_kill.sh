#!/bin/bash

list=$(tmux ls)
new_list="$list"

for i in $new_list
do
  echo "$i"
  sleep 2
  if [[ "$i" == *"attached"* ]]; then
    echo "yes"
  fi
#| awk '{print $10}'
done

