# This Puppet manifest creates a file /tmp/school with specific permissions,
# owner, group, and content.

file { '/tmp/school':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}

