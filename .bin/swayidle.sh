swayidle -w \
    timeout 300 'swaylock --image VGA-1:/home/digo/.wallpapers/vert.png --image HDMI-A-1:/home/digo/.wallpapers/hor.png' \
    timeout 600 'swaymsg "output * power off"' resume 'swaymsg "output * power on"' \
    before-sleep 'swaylock --image VGA-1:/home/digo/.wallpapers/vert.png --image HDMI-A-1:/home/digo/.wallpapers/hor.png'
