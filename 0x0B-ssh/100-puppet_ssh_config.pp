# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 18.233.63.155
    HostName 18.233.63.155
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}

