#!/bin/bash
qtile cmd-obj -o cmd -f windows > ~/.qw-info
st -T qtile-info -e bat ~/.qw-info
