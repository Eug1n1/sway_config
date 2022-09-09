local status_ok, config = pcall(require, "todo-comments")
if not status_ok then
  return
end

config.setup{}
