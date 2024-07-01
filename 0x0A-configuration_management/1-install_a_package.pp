# installation flask from pip3

package { 'python3-pip':
  ensure => installed,
}

package { 'virtualenv':
  ensure => installed,
}

package { 'python3-venv':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}
