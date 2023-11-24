# This manifest kills the process killmenow
exec { 'killmenow_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep killmenow',
}
