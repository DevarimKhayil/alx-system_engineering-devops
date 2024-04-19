# 2-execute_a_command.pp
# Puppet manifest to kill a process named 'killmenow' using the pkill command

exec { 'kill killmenow process':
  command   => '/usr/bin/pkill -f killmenow',
  path      => ['/bin', '/usr/bin'],
  onlyif    => '/usr/bin/pgrep -f killmenow', # Ensures the process is running before attempting to kill it
}

