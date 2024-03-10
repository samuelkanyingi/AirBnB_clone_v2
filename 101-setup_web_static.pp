# puppet manifest
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Hello',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

file { '/data/':
  ensure   => directory,
  owner    => 'ubuntu',
  group    => 'ubuntu',
  recurse  => true,
  require  => File['/data/web_static/releases/test/index.html'],
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

