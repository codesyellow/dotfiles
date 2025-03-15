#!/bin/bash

search_dir="$HOME/.ankivim/decks"

mkdir -p "$search_dir"

folder_name=$(find "$search_dir" -maxdepth 1 -type d | sed "s|$search_dir/||" | tail -n +2 | wofi --dmenu --prompt "")

[ -z "$folder_name" ] && exit

mkdir -p "$folder_path"

foot -T 'ankivim' -a "ankivim" -e anki-vim "$folder_name"
