#!/bin/bash

variant=$(hyprctl devices -j |
  jq -r '.keyboards[] | .active_keymap' | grep intl)

if [[ -n "$variant" ]]; then
  state="warning"
  output=" INTL<span size='15000' foreground='#4c566a'> | </span>"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Keyboar Variant\", \"class\": \"$state\"}"
