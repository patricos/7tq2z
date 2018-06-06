# Test for
# Server program for RPN expression calculator
# by Patryk Mazurkiewicz in Jun 2018
#

import socket

serveripaddr = 'localhost'
serveripport = 8088

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((serveripaddr, serveripport))

clientsocket.send('hello')
response = clientsocket.recv(255)
print response

clientsocket.send('world')
response = clientsocket.recv(255)
print response

clientsocket.send('exit')
response = clientsocket.recv(255)
print response

clientsocket.close()



