#!/usr/bin/python
import socket
import sys
from datetime import datetime
import subprocess

#Clearing your screen
subprocess.call('clear', shell=True)

#Ask for the host to be scanned
host=raw_input("Enter host to be scanned:")
hostip= socket.gethostbyname(host)

#print current scan time
time1=datetime.now()
print "Current scan time is : ",time1

#start the process

try:
  for port in range (1 , 1025):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #Creating a TCP socket
    r = sock.connect_ex((hostip,port))
    if r == 0:
      print"port{}  : Open".format(port)
    sock.close()
except KeyboardInterrupt:    #When u press ctrl+c
  print"Ctrl+c pressed"
  sys.exit()
except socket.gaierror:     #Get address information error
  print "Host not found"
  sys.exit()
except socket.error:
  print"Connection Time out"
  sys.exit()

time2 = datetime.now()
time3 = time2 - time1

print "Total scan time is : " , time3
print "Your scan completed successfully"
  
