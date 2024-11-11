#!/bin/bash

key_variant=$(xkb-switch -p)
if [[ "$key_variant" == "us(intl)" ]]; then
  printf '<span rise="9000" foreground="#EF5A6F" size="30000"></span> <span  rise="16000" foreground="#EF5A6F">INTL</span> <span size="x-large" rise="12000" foreground="#4c566a">|</span>'
fi
