# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

export XDG_RUNTIME_DIR=/run/user/$(id -u)
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export XDG_CURRENT_DESKTOP=Unity
setopt autocd beep extendedglob nomatch

bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/aedigo/.zshrc'

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

# Enable substitution in the prompt.
setopt prompt_subst

# Config for prompt. PS1 synonym.
autoload -Uz compinit colors && colors
#PS1="%{$fg[red]%}%n%{$reset_color%}@%{$fg[blue]%}%m %{$fg[yellow]%}%~ %{$reset_color%}%% "

PROMPT='%{$fg[red]%}%~ %{$fg[white]%}$(git_branch_name) 
'

 if [ "$TERM" = "linux" ]; then
     printf %b '\e[40m' '\e[8]' # set default background to color 0 'dracula-bg'
     printf %b '\e[37m' '\e[8]' # set default foreground to color 7 'dracula-fg'
     printf %b '\e]P0282a36'    # redefine 'black'          as 'dracula-bg'
     printf %b '\e]P86272a4'    # redefine 'bright-black'   as 'dracula-comment'
     printf %b '\e]P1ff5555'    # redefine 'red'            as 'dracula-red'
     printf %b '\e]P9ff7777'    # redefine 'bright-red'     as '#ff7777'
     printf %b '\e]P250fa7b'    # redefine 'green'          as 'dracula-green'
     printf %b '\e]PA70fa9b'    # redefine 'bright-green'   as '#70fa9b'
     printf %b '\e]P3f1fa8c'    # redefine 'brown'          as 'dracula-yellow'
     printf %b '\e]PBffb86c'    # redefine 'bright-brown'   as 'dracula-orange'
     printf %b '\e]P4bd93f9'    # redefine 'blue'           as 'dracula-purple'
     printf %b '\e]PCcfa9ff'    # redefine 'bright-blue'    as '#cfa9ff'
     printf %b '\e]P5ff79c6'    # redefine 'magenta'        as 'dracula-pink'
     printf %b '\e]PDff88e8'    # redefine 'bright-magenta' as '#ff88e8'
     printf %b '\e]P68be9fd'    # redefine 'cyan'           as 'dracula-cyan'
     printf %b '\e]PE97e2ff'    # redefine 'bright-cyan'    as '#97e2ff'
     printf %b '\e]P7f8f8f2'    # redefine 'white'          as 'dracula-fg'
     printf %b '\e]PFffffff'    # redefine 'bright-white'   as '#ffffff'
     clear
 fi

compinit
# End of lines added by compinstall

