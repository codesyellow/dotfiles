#!/bin/sh
hyprctl clients > ~/.text.txt
alacritty --class c_info -e bat ~/.text.txt
