#!/bin/bash

variant=$(hyprctl devices -j |
  jq -r '.keyboards[] | .active_keymap' | grep intl)

if [[ -z "$variant" ]]; then
  state="normal"
  output=" US"
else
  state="critical"
  output=" INTL"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Keyboar Variant\", \"class\": \"$state\"}"
