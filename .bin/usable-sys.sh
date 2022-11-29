#!/bin/sh

curDir=${pwd}

echo 'installing essensials tools using pacman:'; sleep 2
doas pacman --needed -S xorg-server xorg-xset xorg-xmodmap xorg-setxkbmap xorg-xrandr xorg-xprop git base-devel pamixer ttf-font-awesome imlib2 opendoas zsh zsh-completions zsh-syntax-highlighting zsh-autosuggestions neovim easyeffects pipewire pipewire-pulse pipewire pipewire-pulse pipewire-alsa wireplumber pipewire-jack firefox alsa-utils pavucontrol curl steam

echo 'enabling multilib:'; sleep 2
doas nvim /etc/pacman.conf && doas pacman -Syu

echo 'installing some multilib packages:'; sleep 2
# pacman -needed -S lib32-pipewire lib32-pipewire-jack

echo 'enabling services pipewire services:'; sleep 2
# systemctl --user enable --now pipewire pipewire-pulse wireplumber

echo 'disabling mouse acceleration:'; sleep 2
echo '
Section "InputClass"
	Identifier "My Mouse"
	MatchIsPointer "yes"
	Option "AccelerationProfile" "-1"
	Option "AccelerationScheme" "none"
	Option "AccelSpeed" "-1"
EndSection' >> ~/.mouseacc && doas cp -r ~/.mouseacc /etc/X11/xorg.conf.d/50-mouse-acceleration.conf && rm ~/.mouseacc

exit 1
echo 'installing keyd:'; sleep 2
yay -S keyd-git

echo 'installing packer for nvim:'
yay -S nvim-packer-git

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
doas systemctl enable keyd && doas systemctl start keyd

echo 'setting zsh as default:'
# chsh -s /bin/zsh

echo 'installing yay:'
# git clone https://aur.archlinux.org/yay.git
# cd yay && makepkg -sri && cd $curDir

echo 'installing font using yay:'
# yay -S nerd-fonts-cascadia-code

echo 'installing wifi dongle driver using yay:'
# yay -S https://aur.archlinux.org/8188fu-kelebek333-dkms-git.git

echo 'cloning the dotfiles repo to a .dotfiles directory:'
# git clone https://github.com/codesyellow/dotfiles ~/.dotfiles

echo 'coping dotfiles to the home directory:'
# cp -r ~/.dotfiles/. ~/

echo 'installing dwm, st, dmenu and slock:'
# cd ~/.dwm && doas make install
# cd ~/.st && doas make install
# cd ~/.dmenu && doas make install
# cd ~/.slock && doas make install && cd $curDir

echo 'downloading and moving some easyeffects presets:'
#bash -c "$(curl -fsSL https://raw.githubusercontent.com/JackHack96/PulseEffects-Presets/master/install.sh)"
#git clone https://github.com/Rabcor/Heavy-Bass-EE ~/ && mv ~/Heavy-Bass-EE/*.json ~/.config/easyeffects/output

echo 'done!'
