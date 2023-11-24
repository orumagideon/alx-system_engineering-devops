# This installs puppet to install flask vsn 2.1.0 using pip3 installer
package{'flask':
ensure   => '2.1.0',
provider => 'pip3',
}
