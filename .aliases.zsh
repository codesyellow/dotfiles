sud=doas

alias update-grub='$sud grub-mkconfig -o /boot/grub/grub.cfg'
alias nvim='lvim'
alias gtamod='~/.games/gta-sa/modloader/'

alias change_title='xdotool selectwindow set_window --name "scratchpad"'

# dotfiles
alias dotfiles='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias dots='dotfiles push -u origin main'
alias dott='dotfiles status'
alias dotc='dotfiles commit -m'
alias dota='dotfiles add'

# qtile
alias getWInfo='qtile cmd-obj -o cmd -f windows | less'

# arch
alias search='pacman -Ss'
alias lsm="exa -al --color=always --group-directories-first --icons"
alias ls="exa --icons"
alias up='$sud pacman -Syu && gopreload-batch-refresh.sh'
alias i='doas pacman -S'
alias r='$sud pacman -Rs'
alias orphans='$sud pacman -Qtdq | $sud pacman -Rns -'

# make
alias smi='$sud rm config.h; make; $sud make install'

# xclip
alias pbcopy='xclip -selection clipboard'

# zsh
alias sc='$EDITOR ~/.zshrc'
alias sz='source ~/.zshrc'

# configs
alias pc='$EDITOR ~/.config/picom/picom.conf'

# cpupower
alias boost="sudo cpupower frequency-set -g performance"
alias powersave="sudo cpupower frequency-set -g powersave"

# terminal apps
alias sv='sudo -e'
alias v='nvim'
alias vimwiki='nvim ~/.vimwki/index.wiki'

# Anki
alias ae='canki.sh English'
alias ap='canki.sh Portuguese'
alias am='canki.sh Math'

# translate shell
alias t="trans -sp -brief en:pt-br"
alias tb="trans -p -brief pt-br:en"

# translate shell
translate() {
  trans -brief $1:$2 $3
}

re_iso() {
    chdman createcd -i $1 -o $2
}
