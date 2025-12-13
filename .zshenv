set -U PATH path
path=("$HOME/.bin" 
    "$HOME/.cargo/bin" 
    "/usr/sbin:/sbin"
    "$HOME/.projects/python/own" 
    "$HOME/.local/share/cargo/bin"
    "$HOME/.local/bin" 
    "$HOME/.dwm/bar-scripts/" 
    "$HOME/.config/emacs.d/bin" 
    "$HOME/.var/lib/flatpak/exports/share"
    "$HOME/.local/share/gem/ruby/3.2.0/bin"
    "$HOME/.local/share/flatpak/exports/share"
    "$HOME/.nix-profile/bin" "$path[@]")
export PATH

