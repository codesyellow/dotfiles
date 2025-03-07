#!/usr/bin/env python
import sys

actual_structure = ""
EXPAND = "	"

path = sys.argv[1]
name = sys.argv[2]

actual_structure += f"{name} \n"


def add_expand(jumps, content):
    string = ""
    for _ in range(0, jumps):
        string += EXPAND

    return string + content + "\n"


with open(path) as file:
    for line in file.readlines():
        if line.count("*") == 1:
            actual_structure += add_expand(1, line.removeprefix("*").strip())
        elif line.count("**") == 1:
            actual_structure += add_expand(2, line.removeprefix("**").strip())
        elif line.count("-") == 1:
            actual_structure += add_expand(3, line.removeprefix("-").strip())


with open(f"/home/digo/.mindmaps/{name}", "w") as file:
    yes = f"vai \n{EXPAND} oi \n{EXPAND}{EXPAND} yes"
    file.write(actual_structure)
