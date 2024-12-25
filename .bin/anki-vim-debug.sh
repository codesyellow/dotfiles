#!/bin/bash
echo "Running anki-vim" >/tmp/anki-vim-debug.log
echo "Environment:" >>/tmp/anki-vim-debug.log
env >>/tmp/anki-vim-debug.log
echo "Command:" >>/tmp/anki-vim-debug.log
echo "anki-vim /home/digo/.ankivim/decks/portuguese" >>/tmp/anki-vim-debug.log
anki-vim portuguese &>>/tmp/anki-vim-debug.log
