local status_ok, nvim_treehopper = pcall(require, "tsht")
if not status_ok then
  return
end

nvim_treehopper.config.hint_keys = { "h", "j", "f", "d", "n", "v", "s", "l", "a" }
