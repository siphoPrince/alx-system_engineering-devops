# nginx_setup.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80;
        server_name _;

        location / {
            root /var/www/html;
            index index.html;
        }

        location /redirect_me {
            return 301 http://example.com/new_location;
        }
    }
  ",
  notify => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => '<html><body>Hello World!</body></html>',
  require => Package['nginx'],
}
