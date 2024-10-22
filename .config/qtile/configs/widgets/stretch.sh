#!/bin/bash

if [[ -f "/tmp/stretch" ]]; then
    if [[ -f "/tmp/stretch_start" ]]; then
        output=" GET READY!"
        printf '<span foreground="#EF5A6F">%s</span> <span foreground="#fff">|</span>' "$output"
    fi

    if [[ -f "/tmp/stop" ]]; then
        output=" STOP!"
        printf '<span foreground="#EF5A6F">%s</span> <span foreground="#fff">|</span>' "$output"
    else
        output=" DO IT!!"
        printf '<span foreground="#EF5A6F">%s</span> <span foreground="#fff">|</span>' "$output"
    fi
fi
