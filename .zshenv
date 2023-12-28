set -U PATH path
path=("$HOME/.bin" 
    "$HOME/.cargo/bin" 
    "$HOME/.local/share/cargo/bin"
    "$HOME/.local/bin" 
    "$HOME/.emacs.d/bin" 
    "$HOME/.var/lib/flatpak/exports/share"
    "$HOME/.local/share/flatpak/exports/share" "$path[@]"
    "$HOME/.nix-profile/bin" "$path[@]")
export PATH

