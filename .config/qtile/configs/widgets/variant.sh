#!/bin/bash

key_variant=$(xkb-switch -p)
if [[ "$key_variant" == "us(intl)" ]]; then
  printf '<span foreground="#EF5A6F">   INTL </span> <span foreground="#fff">|</span>'
fi
