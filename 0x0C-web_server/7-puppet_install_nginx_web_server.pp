# Puppet manifest to install and configure Nginx web server
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Add rewrite rule for /redirect_me
file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/besthor permanent;',
}

# Ensure Hello World page at /var/www/html/index.html
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Manage Nginx service
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
