#!/bin/bash
df -h | awk '{ if ($6 == "/") print $4 }' | sed 's/G//' >/tmp/root_disk
