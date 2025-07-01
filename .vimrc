call plug#begin()
Plug 'vimwiki/vimwiki'
call plug#end()

syntax enable
set tabstop=2
set number
set hlsearch
set incsearch
let g:netrw_liststyle = 3
let mapleader = " "

map <esc> :noh <CR>

let g:vimwiki_list = [{'path': '~/.vimwiki/',
                      \ 'syntax': 'markdown', 'ext': 'md'}]


