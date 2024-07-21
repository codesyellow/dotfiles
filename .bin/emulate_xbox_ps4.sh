is_active=$(pgrep xboxdrv)

if [[ $1 = 'kill xboxdrv' ]]; then
  notify-send.sh -i ~/.local/share/icons/icons8-xbox-controller-50.png "I've killed xboxdrv, sir!!"
  killall xboxdrv
  exit 1
fi

if [[ -n $is_active ]]; then
  echo 'yes'
  exit 1
else
  echo 'no'
  notify-send.sh -i ~/.local/share/icons/icons8-xbox-controller-50.png 'Xbox joy mode activated'
  xboxdrv --evdev "/dev/input/event18" --evdev-keymap "BTN_SOUTH=a,BTN_EAST=b,BTN_TL=lb,BTN_THUMBR=tr,BTN_SELECT=back,BTN_START=start,BTN_THUMBL=tl,BTN_TR=rb,BTN_NORTH=y,BTN_WEST=x" --evdev-absmap "ABS_RZ=rt,ABS_RY=y2,ABS_RX=x2,ABS_Z=lt,ABS_Y=y1,ABS_X=x1,ABS_HAT0X=dpad_x,ABS_HAT0Y=dpad_y" --axismap "-y2=y2" --mimic-xpad --silent
fi

#doas xboxdrv --evdev "/dev/input/event18" --evdev-keymap "BTN_SOUTH=a,BTN_EAST=b,BTN_TL=lb,BTN_THUMBR=tr,BTN_SELECT=back,BTN_START=start,BTN_THUMBL=tl,BTN_TR=rb,BTN_NORTH=y,BTN_WEST=x" --evdev-absmap "ABS_RZ=rt,ABS_RY=y2,ABS_RX=x2,ABS_Z=lt,ABS_Y=y1,ABS_X=x1,ABS_HAT0X=dpad_x,ABS_HAT0Y=dpad_y" --axismap "-y2=y2,-y1=y1" --mimic-xpad --silent
