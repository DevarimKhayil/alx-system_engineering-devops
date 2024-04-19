# This Puppet manifest installs Flask version 2.1.0 using pip3

exec { 'install Flask':
  command => 'pip3 install Flask==2.1.0',
  unless  => 'pip3 freeze | grep Flask==2.1.0',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}

