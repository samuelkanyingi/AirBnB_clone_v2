# Puppet manifest that sets up your web servers
if ! package { 'nginx':
  ensure => installed,
} {
  exec { 'apt-update':
    command => 'apt-get update',
    path    => '/usr/bin',
    require => Package['nginx'],
  }
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Hello',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

file { '/data/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true,
}

file_line { 'nginx_config':
  path    => '/etc/nginx/sites-enabled/default',
  line    => '    location /hbnb_static { alias /data/web_static/current/; }',
  require => Package['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

