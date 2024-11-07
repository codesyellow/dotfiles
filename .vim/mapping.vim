let mapleader = " "
let g:user_emmet_leader_key=','

nnoremap <silent><esc><esc> :nohlsearch<CR>

nnoremap <leader>pi :IndentLinesToggle<CR>
nnoremap <leader>vs :so %<CR>
nnoremap <leader>aq :q<CR>
nnoremap <leader>aw :w<CR>
nnoremap <leader>wl <C-w>l
nnoremap <leader>wh <C-w>h
nnoremap <leader>wj <C-w>j
nnoremap <leader>wk <C-w>k
nnoremap <leader>bp :bp<CR>
nnoremap <leader>bn :bn<CR>
nnoremap <leader>bd :bd<CR>

" Tab
nnoremap <leader>tp :tabp<CR>
nnoremap <leader>tn :tabn<CR>
nnoremap <s-h> :tabp<CR>
nnoremap <s-l> :tabn<CR>
nnoremap <leader>tc :tabclose<CR>

" VimPlug
nnoremap <leader>ppu :PlugInstall<CR>
nnoremap <leader>ppc :PlugClean<CR>

" NERDTree
nnoremap <silent> <expr> <leader>e g:NERDTree.IsOpen() ? "\:NERDTreeClose<CR>" : bufexists(expand('%')) ? "\:NERDTreeFind<CR>" : "\:NERDTree<CR>"
let NERDTreeCustomOpenArgs={'file':{'where': 't'}}

