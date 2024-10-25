#!/bin/bash

key_variant=$(xkb-switch -p)
if [[ "$key_variant" == "us(intl)" ]]; then
  printf '<span rise="3600" foreground="#EF5A6F">   INTL</span> <span size="x-large" foreground="#fff">|</span>'
fi
