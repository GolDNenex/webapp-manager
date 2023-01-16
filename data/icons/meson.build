application_id = 'it.mijorus.webappmanager'

scalable_dir = join_paths('hicolor', 'scalable', 'apps')
install_data(
  join_paths(scalable_dir, ('@0@.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

actions_dir = join_paths('hicolor', 'scalable', 'actions')
install_data(
  join_paths(actions_dir, 'application-x-executable-symbolic.svg'),
  install_dir: join_paths(get_option('datadir'), 'icons', actions_dir)
)