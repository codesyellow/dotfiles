#!/bin/bash

search_dir="$HOME/.ankivim/decks"

mkdir -p "$search_dir"

folder_name=$(find "$search_dir" -maxdepth 1 -type d \
  | sed "s|$search_dir/||" \
  | tail -n +2 \
  | wmenu -f "Victor Mono Bold Italic 14" -N "#272E33" -n "#D3C6AA" -S "#272E33" -s "#E69875" -i -l "5" -p "AnkiVim")

[ -z "$folder_name" ] && exit

foot -T 'ankivim' -a "ankivim" -e anki-vim "$folder_name"
