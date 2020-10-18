!/usr/bin/python

import socket
host="www.google.com"
port=80

#create a socket
s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#Connect
s.connect((host,port))

#send data
s.send("GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

#receive data
r=s.recv(4096)

print r
