# Changing the configurations of a file name school and inserting contents
file{'/tmp/school':
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
