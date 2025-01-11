-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")

vim.o.shiftwidth = 4

vim.cmd([[
augroup remember_folds
  autocmd!
  autocmd BufWinLeave * mkview
  autocmd BufWinEnter * silent! loadview
augroup END
]])
