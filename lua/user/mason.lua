local status_ok, config = pcall(require, "mason.nvim")
if not status_ok then
    print("mason")
  return
end

config.setup({
	ui = {
		icons = {
			package_installed = "✓",
			package_pending = "➜",
			package_uninstalled = "✗",
		},
	},
})
