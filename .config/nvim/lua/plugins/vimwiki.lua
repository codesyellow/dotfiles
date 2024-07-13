return {
  "vimwiki/vimwiki",
  init = function()
    vim.g.vimwiki_list = {
      {
        path = "~/.vimwiki",
        syntax = "default",
        ext = ".wiki",
      },
    }
  end,
}
