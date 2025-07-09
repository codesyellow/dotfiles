#!/usr/bin/env python3

from i3ipc import Connection, Event
import subprocess

i3 = Connection()
current_output = None


def on_window_focus(i3, e):
    global current_output
    # Get focused workspace
    workspaces = i3.get_workspaces()
    focused_ws = next((ws for ws in workspaces if ws.focused), None)
    if not focused_ws:
        return

    focused_output = focused_ws.output
    if focused_output != current_output:
        current_output = focused_output
        subprocess.run(['polybar-msg', 'action', 'secondary_mon', 'hook', '0'])
        subprocess.run(['polybar-msg', 'action', 'main_mon', 'hook', '0'])
        print(f'Polybar was updated for monitor: {focused_output}')


i3.on(Event.WINDOW_FOCUS, on_window_focus)
i3.main()
