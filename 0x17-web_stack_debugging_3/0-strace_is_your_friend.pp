# Typo in Wordpress config file fix
file { '/var/www/html/wp-includes/class-wp-locale_backup.php':
  ensure => 'file',
  source => '/var/www/html/wp-includes/class-wp-locale.php',
}

file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure  => 'absent',
  require => File['/var/www/html/wp-includes/class-wp-locale_backup.php'],
}

