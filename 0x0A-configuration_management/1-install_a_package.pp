# Install Flask using the package resource

# File: 1-install_a_package.pp

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
}
