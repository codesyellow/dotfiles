call plug#begin()

Plug 'vimwiki/vimwiki'
Plug 'preservim/nerdtree' 
Plug 'ryanoasis/vim-devicons'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'nordtheme/vim'
Plug 'voldikss/vim-floaterm'

call plug#end()

colorscheme nord

set nocompatible
filetype plugin on
syntax on
set autoindent             " Indent according to previous line.
set expandtab              " Use spaces instead of tabs.
set softtabstop =2         " Tab key indents by 2 spaces.
set shiftwidth  =2         " >> indents by 2 spaces.
set shiftround             " >> indents to next multiple of 'shiftwidth'.

set number relativenumber
set nu rnu

set encoding=UTF-8

set backspace   =indent,eol,start  " Make backspace work as you would expect.
set hidden                 " Switch between buffers without having to save first.
set laststatus  =2         " Always show statusline.
set display     =lastline  " Show as much as possible of the last line.

set showmode               " Show current mode in command-line.
set showcmd                " Show already typed keys when more are expected.

set incsearch              " Highlight while searching with / or ?.
set hlsearch               " Keep matches highlighted.

set ttyfast                " Faster redrawing.
set lazyredraw             " Only redraw when necessary.

set splitbelow             " Open new windows below the current window.
set splitright             " Open new windows right of the current window.

set cursorline             " Find the current line quickly.
set wrapscan               " Searches wrap around end-of-file.
set report      =0         " Always report changed lines.
set synmaxcol   =200       " Only highlight the first 200 columns.

let mapleader = " " 
nnoremap <C-n> :NERDTree<CR>
nnoremap <leader>n :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
nnoremap <C-f> :<CR>
" Configuration example
let g:floaterm_keymap_new    = '<leader>tc'
let g:floaterm_keymap_prev   = '<leader>tn'
let g:floaterm_keymap_next   = '<leader>tp'
let g:floaterm_keymap_toggle = '<leader>u'

