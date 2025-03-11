#!/usr/bin/env python
import sys

actual_structure = ""
EXPAND = "	"
child_jump = 0

path = sys.argv[1]
name = sys.argv[2]
level = 0

actual_structure += f"{name} \n"


def add_expand(jumps, content):
    string = ""
    for _ in range(0, jumps):
        string += EXPAND

    return string + content + "\n"


# remove prefix corretly
with open(path) as file:
    for line in file.readlines():
        if line.count("*") >= 1:
            actual_structure += add_expand(line.count("*"),
                                           line.removeprefix("*" * line.count("*")).strip())
            child_jump = line.count("*")
        elif line.count("-") == 1:
            actual_structure += add_expand(child_jump,
                                           line.removeprefix("-").strip())


with open(f"/home/digo/.mindmaps/{name}", "w") as file:
    file.write(actual_structure)
