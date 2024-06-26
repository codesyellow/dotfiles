#!/bin/sh
userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
	xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
	xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
	xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
	xmodmap "$usermodmap"
fi

# start some nice programs

#if [ -d $HOME/.xinitrc.d ]; then
#	for f in $HOME/.xinitrc.d/?*.sh; do
#		[ -x "$f" ] && . "$f"
#	done
#	unset f
#fi

while true; do
	dwm-bar.sh
	sleep 1s
done &

exec startdwm
