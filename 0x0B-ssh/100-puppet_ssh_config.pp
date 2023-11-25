#using pup to acces withou password
include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/home/your_username/.ssh/config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/home/your_username/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}

