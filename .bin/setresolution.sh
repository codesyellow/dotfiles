#!/bin/bash
xrandr --newmode "1360x768_60.00" 85.25 1360 1440 1576 1792 768 771 781 798 -hsync +vsync
xrandr --addmode HDMI-1 "1360x768_60.00"
xrandr --output HDMI-1 --mode "1360x768_60.00"
