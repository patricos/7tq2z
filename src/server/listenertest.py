# Test for
# Server program for RPN expression calculator
# by Patryk Mazurkiewicz in Jun 2018
#

import socket   # socket #class
import time     # time.sleep(seconds)
import os       # os.getpid()

serveripaddr = 'localhost'
serveripport = 8088
commands = ["hello world", "a", "b", "c", "end"]
procid = str( os.getpid() ) + ": "


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((serveripaddr, serveripport))

for x in range(0, len(commands)):
    clientsocket.send(  procid + commands[x]  )
    response = clientsocket.recv(255)
    print response
    time.sleep(3)

time.sleep(3)
clientsocket.close()

