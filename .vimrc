source ~/.vim/plugins.vim
source ~/.vim/defaults.vim
source ~/.vim/plugins_configs.vim
source ~/.vim/mapping.vim

au BufEnter,BufRead *conf* setf dosini

"set clipboard=unnamed,unnamedplus
"
"augroup wl-clipboard
"    autocmd!
"    autocmd FocusLost * :call system('wl-copy --trim-newline', @+)
"    autocmd FocusGained * :let @+ = system('wl-paste -n')
"augroup END
