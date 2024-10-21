# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

export XDG_DATA_HOME=$HOME/.local/share
export XDG_CONFIG_HOME=$HOME/.config
export XDG_STATE_HOME=$HOME/.local/state
export XDG_CACHE_HOME=$HOME/.cache
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export TERM="screen-256color"
export EDITOR=/usr/bin/vim
export CM_LAUNCHER=dmenu
export VISUAL=/usr/bin/vim
setopt autocd beep extendedglob nomatch
export NNN_USE_EDITOR=1
export NNN_OPENER=zathura

bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/aedigo/.zshrc'
zstyle :compinit -d "$XDG_CACHE_HOME"/zsh/zcompdump-"$ZSH_VERSION"

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.aliases.zsh

bindkey -M viins 'jk' vi-cmd-mode

zstyle ':completion:*'  matcher-list 'm:{a-z}={A-Z}'

bindkey '^ ' autosuggest-accept

# Find and set branch name var if in git repository.
function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo '('$branch')'
  fi
}

# pipe it to less
function l { $@ | less }

# Enable substitution in the prompt.
setopt prompt_subst

# Config for prompt. PS1 synonym.
autoload -Uz compinit colors && colors
#PS1="%{$fg[red]%}%n%{$reset_color%}@%{$fg[blue]%}%m %{$fg[yellow]%}%~ %{$reset_color%}%% "

PROMPT='%{$fg[red]%}%~ %{$fg[white]%}$(git_branch_name) 
'
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=5'
compinit
eval "$(zoxide init zsh)"
# End of lines added by compinstall
