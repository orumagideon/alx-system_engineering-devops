# Ensure the correct content in wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  replace => true,
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
  notify  => Service['apache2'],
}

# Ensure Apache service is running and restarted when wp-settings.php changes
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/wp-settings.php'],
}
