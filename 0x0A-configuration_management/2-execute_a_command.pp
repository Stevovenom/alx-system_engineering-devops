# 2-execute_a_command.pp

exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  onlyif  => 'pgrep -f killmenow',
}
