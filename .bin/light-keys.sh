keyboard_number=$(ls -l /dev/input/by-id | grep 'usb-SEMICO_USB_Keyboard-event-kbd' | awk "NR==1{print;exit}" | sed 's/.*\(..\)$/\1/' | sed 's/[^0-9]*//g')

doas python ~/.bin/ledToggler.py /dev/input/event$keyboard_number scrolllock scrolllock 1 1 &
