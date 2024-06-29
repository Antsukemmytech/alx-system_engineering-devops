#Using Puppet install flask from pip3
	packgage { 'Flask":
	ensure => '2.1.0',
	provider => 'pip3',
}

