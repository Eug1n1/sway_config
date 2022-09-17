-- local cmp_status_ok, colorscheme = pcall(require, "ayu")
-- if not cmp_status_ok then
--   return
-- end

vim.cmd([[
try
  colorscheme gruvbox
  set background=light
catch /^Vim\%((\a\+)\)\=:E185/
  colorscheme default
  set background=dark
endtry
]])

-- colorscheme.colorscheme()

-- colorscheme.setup({
--     overrides = {
--         default = { bg = "#0f1419" },
--     }
-- })
