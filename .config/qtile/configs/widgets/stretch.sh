#!/bin/bash

if [[ -f "/tmp/stretch" ]]; then
    if [[ -f "/tmp/stretch_start" ]]; then
        output=" GET READY!"
        printf '<span rise="3600" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' "$output"
    fi

    if [[ -f "/tmp/stop" ]]; then
        output=" STOP!"
        printf '<span rise="3600" foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' "$output"
    else
        output=" DO IT!!"
        printf '<span rise="3600 "foreground="#EF5A6F">%s</span> <span size="x-large" foreground="#fff">|</span>' "$output"
    fi
else
    printf ''
fi
