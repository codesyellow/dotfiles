#!/bin/bash

resx=1360
resy=768

winx=$1
winy=$2

xResult=$(((resx - winx) / 2))
yResult=$(((resy - winy) - 20))
echo "$xResult"
echo "$yResult"
