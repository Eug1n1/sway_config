vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.signcolumn = 'yes'
vim.opt.smarttab = true
vim.opt.termguicolors = true
vim.opt.hidden = true
vim.opt.updatetime = 300
vim.opt.encoding = 'utf-8'
vim.opt.autoindent = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.softtabstop = 4
vim.opt.expandtab = true
vim.opt.backup = false                         -- creates a backup file
vim.opt.clipboard = "unnamedplus"
vim.opt.completeopt = { "menuone", "noselect" } -- mostly just for cmp
vim.opt.conceallevel = 0                        -- so that `` is visible in markdown files
vim.opt.swapfile = false
vim.opt.cursorline = true
vim.opt.colorcolumn = '75'
vim.opt.undofile = true
vim.opt.wrap = true

require 'configs.plugins'
require 'configs.lualine'
require 'configs.treesitter'
require 'configs.cmp'
require 'configs.colorscheme'
require 'configs.autopairs'
require 'configs.nvim-tree'
require 'configs.keymaps'
require 'configs.hop'
require 'configs.nvim-treehopper'

local map = vim.api.nvim_set_keymap

map('i', 'jk', '<esc>', {})

local options = { noremap = true }

map('n', 'ff', ':Telescope find_files<cr>', options)
map('n', 'fb', ':Telescope buffers<cr>', options)
map('n', 'fgf', ':Telescope git_files<cr>', options)
map('n', 'fgc', ':Telescope git_commits<cr>', options)
map('n', 'fgb', ':Telescope git_branches<cr>', options)


vim.api.nvim_set_keymap('n', 'f', "<cmd>lua require'hop'.hint_char1({ direction = require'hop.hint'.HintDirection.AFTER_CURSOR, current_line_only = true })<cr>", {})
vim.api.nvim_set_keymap('n', 'F', "<cmd>lua require'hop'.hint_char1({ direction = require'hop.hint'.HintDirection.BEFORE_CURSOR, current_line_only = true })<cr>", {})
vim.api.nvim_set_keymap('o', 'f', "<cmd>lua require'hop'.hint_char1({ direction = require'hop.hint'.HintDirection.AFTER_CURSOR, current_line_only = true, inclusive_jump = true })<cr>", {})
vim.api.nvim_set_keymap('o', 'F', "<cmd>lua require'hop'.hint_char1({ direction = require'hop.hint'.HintDirection.BEFORE_CURSOR, current_line_only = true, inclusive_jump = true })<cr>", {})
vim.api.nvim_set_keymap('', 't', "<cmd>lua require'hop'.hint_char1({ direction = require'hop.hint'.HintDirection.AFTER_CURSOR, current_line_only = true })<cr>", {})
vim.api.nvim_set_keymap('', 'T', "<cmd>lua require'hop'.hint_char1({ direction = require'hop.hint'.HintDirection.BEFORE_CURSOR, current_line_only = true })<cr>", {})
vim.api.nvim_set_keymap('n', '<leader>e', "<cmd> lua require'hop'.hint_words({ hint_position = require'hop.hint'.HintPosition.END })<cr>", {})
vim.api.nvim_set_keymap('v', '<leader>e', "<cmd> lua require'hop'.hint_words({ hint_position = require'hop.hint'.HintPosition.END })<cr>", {})
vim.api.nvim_set_keymap('o', '<leader>e', "<cmd> lua require'hop'.hint_words({ hint_position = require'hop.hint'.HintPosition.END, inclusive_jump = true })<cr>", {})
