# Test for
# Logging server for multiprocess file logging
# by Patryk Mazurkiewicz in Jun 2018
#

import socket   # socket #class
import time     # time.sleep(seconds)
import os       # os.getpid()

serveripaddr = 'localhost'
serveripport = 8089
commands = ["hello world", "a", "b", "c", "end"]
procid = str( os.getpid() ) + ": "


for x in range(0, len(commands)):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((serveripaddr, serveripport))
    clientsocket.send(  procid + commands[x]  )
    clientsocket.close()

