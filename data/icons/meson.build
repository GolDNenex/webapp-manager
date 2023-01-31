application_id = 'it.mijorus.webappmanager'

scalable_dir = join_paths('hicolor', 'scalable', 'apps')
install_data(
  join_paths(scalable_dir, ('@0@.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

# action_dir = join_paths('hicolor', 'scalable', 'actions')
# action_icons = [
#     join_paths(action_dir, 'executable.svg'),
# ]

# install_data(
#   action_icons,
#   install_dir: join_paths(get_option('datadir'), 'icons', action_dir)
# )