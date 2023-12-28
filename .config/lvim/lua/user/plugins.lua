lvim.plugins = {
  {
    "nvim-neorg/neorg",
    ft = "norg", -- lazy-load on filetype
    config = true, -- run require("neorg").setup()
  },
  {
    "neanias/everforest-nvim",
    version = false,
    lazy = false,
    priority = 1000, -- make sure to load this before all the other start plugins
  },
  {
    "luckasRanarison/tree-sitter-hypr",
  },
  {
    'barrett-ruth/live-server.nvim',
    build = 'yarn global add live-server',
    config = true
  },
  { 'nvim-focus/focus.nvim', version = false },
}
