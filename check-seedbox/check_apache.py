#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket, subprocess
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip="127.0.0.1"
port="80"
try:
	s.connect((ip, int(port)))
	s.shutdown(2)
	print "Apache is running"
except:
	print "Apache not responding"
	subprocess.call(['/etc/init.d/apache2', 'start'])
