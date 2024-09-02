return {
  "nvim-neorg/neorg",
  lazy = false, -- Disable lazy loading as some `lazy.nvim` distributions set `lazy = true` by default
  version = "*", -- Pin Neorg to the latest stable release
  config = true,
  opts = {
    load = {
      ["core.defaults"] = {},
      ["core.keybinds"] = {
        config = {
          neorg_leader = ",",
          hook = function(keybinds)
            keybinds.remap_event("norg", "n", "<leader>tu", "core.qol.todo_items.todo.task_undone")
            keybinds.remap_event("norg", "n", "<leader>tp", "core.qol.todo_items.todo.task_pending")
            keybinds.remap_event("norg", "n", "<leader>td", "core.qol.todo_items.todo.task_done")
            keybinds.remap_event("norg", "n", "<leader>th", "core.qol.todo_items.todo.task_hold")
            keybinds.remap_event("norg", "n", "<leader>tc", "core.qol.todo_items.todo.task_cancelled")
            keybinds.remap_event("norg", "n", "<leader>tr", "core.qol.todo_items.todo.task_recurring")
            keybinds.remap_event("norg", "n", "<leader>ti", "core.qol.todo_items.todo.task_important")
            keybinds.remap_event("norg", "n", "<leader>ta", "core.qol.todo_items.todo.task_ambiguous")
          end,
        },
      },
      ["core.concealer"] = {}, -- We added this line!
      ["core.dirman"] = {
        config = {
          workspaces = {
            notes = "~/.notes/",
          },
          default_workspace = "notes",
        },
      },
    },
  },
}
