# Apache 500 Error Resolution using Puppet

## Task Description
In this exercise, the goal is to identify and resolve a 500 Internal Server Error in an Apache web server using strace for debugging and then automate the fix using Puppet.

## Instructions
1. Use `strace` to find out why Apache is returning a 500 error.
   - `strace` can be attached to a currently running process.
   - Consider using `tmux` to run `strace` in one window and `curl` in another.

2. Identify the issue causing the 500 error and fix it.

3. Write a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix.
   - Use any Puppet resource type to implement the solution.

## Example
```bash
# Initial 500 error
curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error

# Apply Puppet manifest to fix the error
puppet apply 0-strace_is_your_friend.pp

# Verify the fix
curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Puppet Manifest Explanation
The Puppet manifest (0-strace_is_your_friend.pp) provided resolves the issue by correcting a string in the wp-settings.php file and restarting the Apache service.

puppet
Copy code
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
This Puppet code follows Puppet best practices for managing file content and services, ensuring idempotence and proper dependencies
