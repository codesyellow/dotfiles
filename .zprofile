if [ -z "$DISPLAY" ] && [ "$XDG_VTNR" = 1 ]; then
  niri-session -l
fi
