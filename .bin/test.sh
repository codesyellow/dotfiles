#!/bin/bash
# One line for i3config :
exec_always --no-startup-id i3-msg -t subscribe -m '[ "window" ]' | while read line ; do if [ $(echo $line | awk '/"class":"steam","instance":"steamwebhelper"/{print}') ]; then i3-msg '[class="steam"] border pixel 1' && sleep 1 && i3-msg '[class="steam"] border pixel 2'; fi; done

# Better indentation (to put in a script if you prefer)
i3-msg -t subscribe -m '[ "window" ]' |\
	while read line ; do
		if [ $(echo $line | awk '/"class":"steam","instance":"steamwebhelper"/{print}') ]; then
			i3-msg '[class="steam"] border pixel 1'
			sleep 1
			i3-msg '[class="steam"] border pixel 2'
		fi;
	done
