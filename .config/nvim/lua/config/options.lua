-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here
vim.g.lazyvim_python_lsp = "pyright"
vim.g.maplocalleader = ";"
vim.o.shiftwidth = 4 -- Number of spaces inserted when indenting
vim.opt.foldmethod = "manual"

vim.cmd([[
augroup remember_folds
  autocmd!
  autocmd BufWinLeave * mkview
  autocmd BufWinEnter * silent! loadview
augroup END
]])
