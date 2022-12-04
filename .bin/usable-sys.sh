#!/bin/sh
sud=doas
curDir=${pwd}
pkg='xorg-server xorg-xset xorg-xmodmap xorg-setxkbmap xorg-xrandr xorg-xprop git base-devel pamixer ttf-font-awesome imlib2 opendoas zsh zsh-completions zsh-syntax-highlighting zsh-autosuggestions neovim easyeffects pipewire pipewire-pulse pipewire pipewire-pulse pipewire-alsa wireplumber pipewire-jack firefox alsa-utils pavucontrol curl steam calf irqbalance earlyoom git github-cli libva-intel-driver libva-vdpau-driver libva-utils vdpauinfo lib32-pipewire lib32-pipewire-jack heroic-games-launcher-bin linux-tkg-bmq linux-tkg-bmq-headers wine-tkg-staging-fsync-git bottles gamemode lib32-gamemode lxappearance-gtk3 translate-shell espeak-ng mpv yt-dlp'

yayPkg='mangohud-git keyd-git nvim-packer-git ananicy-cpp xidlehook-git nerd-fonts-cascadia-code googledot-cursor-theme notify-send.sh'

function startService() {
  systemctl enable --now "$@"
}

function startUserService() {
  systemctl --user enable --now "$@" 
}

function printing() {
  echo $1':'; sleep 2
}

function append() {
  echo $1 | sudo tee -a $2; sleep 2
}

function chaotic() {
  $sud pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
  $sud pacman-key --lsign-key FBA220DFC880C036
  $sud pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
  append '
  [chaotic-aur]
  Include = /etc/pacman.d/chaotic-mirrorlist' /etc/pacman.conf
}

function packages() {
  echo "$@"
  doas pacman --needed -S "$@"
}

function zram() {
  echo 'zram' | sudo tee -a /etc/modules-load.d/zram.conf; sleep 2
  echo 'options zram num_devices=4' | sudo tee -a /etc/modprobe.d/zram.conf 
  echo 'KERNEL=="zram0", ATTR{disksize}="512M" RUN="/usr/bin/mkswap /dev/zram0", TAG+="systemd"
  KERNEL=="zram1", ATTR{disksize}="512M" RUN="/usr/bin/mkswap /dev/zram1", TAG+="systemd"
  KERNEL=="zram2", ATTR{disksize}="512M" RUN="/usr/bin/mkswap /dev/zram2", TAG+="systemd"
  KERNEL=="zram3", ATTR{disksize}="512M" RUN="/usr/bin/mkswap /dev/zram3", TAG+="systemd"' | sudo tee -a /etc/udev/rules.d/99-zram.rules
  echo '/dev/zram0 none swap defaults 0 0
  /dev/zram1 none swap defaults 0 0
  /dev/zram2 none swap defaults 0 0
  /dev/zram3 none swap defaults 0 0' | sudo tee -a /etc/fstab
}

printing 'installing chaotic aur'
#chaotic

printing 'enabling multilib'
#doas nvim /etc/pacman.conf && doas pacman -Syu

echo 'installing essensials tools using pacman:'; sleep 2
packages $pkg

printing 'installing yay'
#git clone https://aur.archlinux.org/yay.git
#cd yay && makepkg -sri && cd $curDir

printing 'installing packages from yay'
yay -S --noconfirm --nocleanmenu --nodiffmenu $yayPkg --needed

printing 'installing nord theme gtk'
mkdir ~/.themes
git clone https://github.com/EliverLara/Nordic ~/.themes/nordic

lxappearance
exit 1
printing 'enabling user services'
startUserService pipewire pipewire-pulse wireplumber

printing 'enabling system service'
startService ananicy-cpp irqbalance earlyoom

printing 'kernel parameters. read the filer ~/.paremeters for reference'
echo 'mitigation=off resume=UUID=61ad2324-f01d-4f57-94bc-494139d13cb7 nowatchdog' >> ~/.parameters && doasedit /etc/default/grub
rm ~/.parameters

printing 'video acceleration'
append 'VDPAU_DRIVER=va_gl' '/etc/environment'
vainfo | less
vdpauinfo | less
$sud pacman -Rs vdpauinfo libva-utils

echo 'disabling mouse acceleration:'; sleep 2
echo '
Section "InputClass"
	Identifier "My Mouse"
	MatchIsPointer "yes"
	Option "AccelerationProfile" "-1"
	Option "AccelerationScheme" "none"
	Option "AccelSpeed" "-1"
EndSection' >> ~/.mouseacc && doas cp -r ~/.mouseacc /etc/X11/xorg.conf.d/50-mouse-acceleration.conf && rm ~/.mouseacc

echo 'configuring keyd:'
echo '[ids]

*

[main]

shift = oneshot(shift)
meta = oneshot(meta)
control = oneshot(control)

leftalt = oneshot(alt)
rightalt = oneshot(altgr)

capslock = overload(control, esc)
insert = S-insert' >> ~/.keyd.conf
doas ln -s ~/.keyd.conf /etc/keyd/default.conf

echo 'enabling keyd service:'
startService keyd; sleep 2
# this is cuz keyd changes my keyboard layout and mod keyd
setxkbmap -layout "br(nodeadkeys),br" -option "grp:alt_shift_toggle"
xmodmap ~/.Xmodmap

echo 'setting zsh as default:'
chsh -s /bin/zsh

echo 'installing wifi dongle driver using yay:'
yay -S https://aur.archlinux.org/8188fu-kelebek333-dkms-git.git

printing 'cloning the bare repo'
echo ".cfg" ~/.gitignore
git clone --bare https://github.com/codesyellow/dotfiles ~/.cfg
dotfiles checkout

echo 'cloning the dotfiles repo to a .dotfiles directory:'
git clone https://github.com/codesyellow/dotfiles ~/.dotfiles

echo 'coping dotfiles to the home directory:'
cp -r ~/.dotfiles/. ~/

echo 'installing dwm, st, dmenu and slock:'
cd ~/.dwm && doas make install
cd ~/.st && doas make install
cd ~/.dmenu && doas make install
cd ~/.slock && doas make install && cd $curDir

echo 'downloading and moving some easyeffects presets:'
bash -c "$(curl -fsSL https://raw.githubusercontent.com/JackHack96/PulseEffects-Presets/master/install.sh)"
git clone https://github.com/Rabcor/Heavy-Bass-EE ~/ && mv ~/Heavy-Bass-EE/*.json ~/.config/easyeffects/output

# alsamixer

echo 'uninstalling sudo:'; sleep 2
doas pacman -Rs sudo
echo 'done!'
