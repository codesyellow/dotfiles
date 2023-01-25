set -U PATH path
path=("$HOME/.bin" 
    "$HOME/.cargo/bin" 
    "$HOME/.local/bin" 
    "$HOME/.emacs.d/bin" 
    "$HOME/var/lib/flatpak/exports/share"
    "$HOME/home/cse/.local/share/flatpak/exports/share" "$path[@]")
export PATH

