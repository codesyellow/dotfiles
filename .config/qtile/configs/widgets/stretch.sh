#!/bin/bash

if [[ -f "/tmp/stretch" ]]; then
    if [[ -f "/tmp/stretch_start" ]]; then
        output=" GET READY!"
        printf '<span size="x-large" foreground="#4c566a">| </span><span rise="3600" foreground="#EF5A6F">%s</span>'  "$output"
    fi

    if [[ -f "/tmp/stop" ]]; then
        output=" STOP!"
        printf '<span size="x-large" foreground="#4c566a">| </span><span rise="3600" foreground="#EF5A6F">%s</span>' "$output"
    else
        output=" DO IT!!"
        printf '<span size="x-large" foreground="#4c566a">| </span><span rise="3600" foreground="#EF5A6F">%s</span>' "$output"
    fi
else
    printf ''
fi
