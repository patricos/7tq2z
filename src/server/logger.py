# Logging server for multiprocess file logging
# by Patryk Mazurkiewicz in Jun 2018
#
# This works by buffering the incomming messages from multiprocessing
# threads and by flushing this buffer/queue serially into the file.
# Will log port scanning too, I guess...  Quick and dirty and working.
# Put your safety squints on, please.
#

import socket       # s.socket, s.bind, s.listen, s.send, s.recv
import os           # os.getpid()

loggeripaddr = 'localhost'                  # = socket.gethostname()
loggeripport = 8089
logfilefpath = '../../../server.log'        # will work when called from the repo, but beware!

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # creates socket object of AF_INET family and SOCK_STREAM type
s.bind((loggeripaddr, loggeripport))                               # configs the socket for a particular srv socket (address:port)
s.listen(5)                                                        # length of queue for connections waiting to be accept()-ed

print 'Log PID is: ' + str(os.getpid())                            # whoami for debugging purposes

while True:                                                        # loop for listening
    connection, address = s.accept()
    readbuf = connection.recv(1024)                                # reads up to a specified number of bytes of data
    connection.close()

    # Now writing the whole received message to the log.
    file = open(logfilefpath,"a")
    file.write(readbuf)
    file.close()

s.shutdown(socket.SHUT_RDWR)
s.close()
print 'Bye bye.'

