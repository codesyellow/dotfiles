#!/bin/bash

# Function to list available directories and files, and then search for and open a folder with Anki-Vim
open_folder_with_anki() {
  # List available directories and files in ~/.ankivim/decks
  echo "Available directories and files in ~/.ankivim/decks:"
  ls -l ~/.ankivim/decks

  read -p "Enter the name of the folder you want to open or create: " foldername

  # Change directory to ~/.ankivim/decks
  cd ~/.ankivim/decks || { echo "Error: Directory not found."; exit 1; }

  # Check if the folder already exists
  if [[ -d "$foldername" ]]; then
    echo "Folder '$foldername' already exists in ~/.ankivim/decks."
  else
    # If the folder does not exist, create it
    mkdir "$foldername"
    echo "Folder '$foldername' created in ~/.ankivim/decks."
  fi

  # Open Anki-Vim in the same Alacritty instance
  anki-vim "$foldername"

  # Ask if the user wants to open another folder
  read -p "Do you want to open another folder? (Y/N): " choice
  case "$choice" in
    y|Y ) open_folder_with_anki ;; # Open another folder if user chooses yes
    n|N ) echo "Exiting script." ;; # Exit script if user chooses no
    * ) echo "Invalid input. Exiting script." ;; # Handle invalid input
  esac
}

# Start the script by listing available directories and files, and then searching for and opening a folder or creating a new folder with Anki-Vim in ~/.ankivim/decks
open_folder_with_anki

