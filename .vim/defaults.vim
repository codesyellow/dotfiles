autocmd BufNewFile,BufRead * if match(getline(1),"node") >= 0 | set filetype=javascript | endif
set nocompatible
set clipboard=unnamedplus
set foldmethod=manual

filetype plugin indent on  " Load plugins according to detected filetype.
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
set nowrap
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
colorscheme nord
set number
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave,WinEnter * if &nu && mode() != "i" | set rnu   | endif
  autocmd BufLeave,FocusLost,InsertEnter,WinLeave   * if &nu                  | set nornu | endif
augroup END


" Enable auto completion menu after pressing TAB.
set wildmenu

" Make wildmenu behave like similar to Bash completion.
set wildmode=list:longest

" There are certain files that we would never want to edit with Vim.
" Wildmenu will ignore files with these extensions.
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

set colorcolumn=100
hi ColorColumn ctermbg=darkgray 
" this will make sure .wiki files dont have the ruller
autocmd BufRead,BufNewFile *.wiki set filetype=wiki
autocmd FileType wiki setlocal colorcolumn=0
