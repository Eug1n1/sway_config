local status_ok, kommentary = pcall(require, "kommentary.config")
if not status_ok then
  return
end

kommentary.use_extended_mappings()

kommentary.configure_language("default", {
    prefer_single_line_comments = true,
})
