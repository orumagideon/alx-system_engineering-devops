#!/usr/bin/env bash
# Configure server using puppet

# Puppet class called nginx_server that 
# Configuration for the Nginx server.
class nginx_server {
  package { 'nginx':
    ensure => installed,
  }

#  manages the Nginx service.
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
# manages the Nginx configuration file located at /etc/nginx/sites-available/default.
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "
      server {
        listen      80 default_server;
        listen      [::]:80 default_server;
        root        /var/www/html;
        index       index.html index.htm;

        location / {
          return 200 'Hello World!';
        }

        location /redirect_me {
          return 301 http://cuberule.com/;
        }
      }
    ",
    notify => Service['nginx'],
  }
}
#  Nginx_server class, ensuring that it gets applied.
include nginx_server
