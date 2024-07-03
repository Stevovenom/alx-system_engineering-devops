!#/usr/bin/env bash
# using puppet to make changes to our configuration file

file { 'etc/ssh/config':
  ensure  => present,
  content => "
  #ssh user configuration
  host*
  IdentifyFile ~/.ssh/school
  PasswordAuthentication no
  ",
}
