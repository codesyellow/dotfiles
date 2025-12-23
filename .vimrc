call plug#begin()
Plug 'vimwiki/vimwiki'
Plug 'sainnhe/gruvbox-material'
Plug 'jasonccox/vim-wayland-clipboard'
call plug#end()

set nocompatible
set foldmethod=manual
filetype plugin indent on  " Load plugins according to detected filetype.
set clipboard=unnamedplus
syntax on                  " Enable syntax highlighting.
set autoindent             " Indent according to previous line.
set expandtab              " Use spaces instead of tabs.
set softtabstop =2         " Tab key indents by 4 spaces.
set shiftwidth  =2         " >> indents by 4 spaces.
set shiftround             " >> indents to next multiple of 'shiftwidth'.
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
set scrolloff=10           " Make cursor not get close to the bottom
set splitbelow             " Open new windows below the current window.
set splitright             " Open new windows right of the current window.
set laststatus=2
set noshowmode
set ignorecase             " match everything
"set wrap
set smartcase              " this override ignorecase and search, for example, for upper case only
set showmatch
set cursorline             " Find the current line quickly.
set cursorcolumn
set wrapscan               " Searches wrap around end-of-file.
set report      =0         " Always report changed lines.
set synmaxcol   =200       " Only highlight the first 200 columns.
set termguicolors
set history=1000
set background=dark
colorscheme gruvbox-material
set number

map <esc> :noh <CR>

let g:vimwiki_list = [{'path': '~/.vimwiki/',
                      \ 'syntax': 'markdown', 'ext': 'md'}]

