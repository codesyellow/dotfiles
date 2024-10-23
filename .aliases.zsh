sud=sudo

function :wi() {
  xprop | awk '
  /^WM_CLASS/{sub(/.* =/, "instance:"); sub(/,/, "\nclass:"); print}
  /^WM_NAME/{sub(/.* =/, "title:"); print}'
}

alias change_title='xdotool selectwindow set_window --name "scratchpad"'
alias change_class='xdotool selectwindow set_window --class "esdf"'

alias lp='{(comm -23 <(yay -Qqe | sort) <({(pactree -u -d 1 base)&&(yay -Qqg base-devel);} | sort))&&(comm -23 <(yay -Qqtt | sort) <(yay -Qqt | sort));} | sort | uniq  | less'

# defaults
alias :c='clear'
alias cd='z'
alias :m='mkdir -p'
alias :fp='chmod +x'
alias :tx='tar xvf'
alias :r='rm'
alias :rr='rm -rf'

# systemctl
alias :st="systemctl --user start"
alias :ss="systemctl --user status"
alias :sp="systemctl --user stop"
alias :sr="systemctl --user restart"
alias :sd="systemctl --user daemon-reload"

# tmux
alias :tl="tmux ls"

# dotfiles
:dotfiles() {
  /usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME "$@"
}

:dd() {
  :dotfiles diff
}

:ds() {
  :dotfiles push -u origin main
}

:dt() {
  :dotfiles status
}

:dc() {
  :dotfiles commit -m "$@"
}

:da() {
  :dotfiles add "$@"
}

# qtile
alias getWInfo='qtile cmd-obj -o cmd -f windows | less'

# arch
alias search='pacman -Ss'
alias lsm="exa -al --color=always --group-directories-first --icons"
alias ls="exa --icons"
alias :pu='yay'
alias :ps='pacman -Ss'
alias :pi='sudo pacman -S'
alias :pr='sudo pacman -Rs'
alias :po='$sud pacman -Qtdq | $sud pacman -Rns -'

alias :fi='flatpak install'
alias :fu='flatpak update'
alias :fr='flatpak uninstall'

# make
alias smi='$sud rm config.h; make; $sud make install'

# xclip
alias pbcopy='xclip -selection clipboard'

# zsh
alias :sc='vim ~/.zshrc'
alias :sz='source ~/.zshrc'

# configs
alias :cp='$EDITOR ~/.config/picom/picom.conf'
alias :cz='$EDITOR ~/.zshrc'
alias :cza='$EDITOR ~/.aliases.zsh'
alias :czp='$EDITOR ~/.zshenv'
alias :cq='$EDITOR ~/.config/qtile/config.py'
alias :cv='$EDITOR ~/.vimrc'
alias :cvd='$EDITOR ~/.vim/defaults.vim'

# cpupower
alias boost="sudo cpupower frequency-set -g performance"
alias powersave="sudo cpupower frequency-set -g powersave"

# terminal apps
alias :v='$EDITOR'
alias :V='sudoedit'

# translate shell
alias :t="trans -sp -brief en:pt-br"
alias :tb="trans -p -brief pt-br:en"

# translate shell
translate() {
  trans -brief $1:$2 $3
}

:chd() {
    chdman createcd -i $1 -o $2
}
