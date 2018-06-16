# Server program for RPN expression calculator
# by Patryk Mazurkiewicz in Jun 2018
#
# OKAY: listens
# todo: sanitize the input (ascii, perhaps limited ser of characters)
# OKAY: properly shut the socket disused
# todo: parses input
# todo: registers timings
# todo: logs timings and necessary things
# todo: spawns workers
# todo: receives results from worker
# OKAY: sends results back

import socket       # s.socket, s.bind, s.listen, s.send, s.recv
import thread       # thread.start_new_thread()
import os           # os.getpid()
import time         # time.time()
import subprocess   # subprocess.Popen(), process.communicate()

serveripaddr = 'localhost'                                         # = socket.gethostname()
serveripport = 8088
workerfulpat = '../worker/rpnworker'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # creates socket object of AF_INET family and SOCK_STREAM type
s.bind((serveripaddr, serveripport))                               # configs the socket for a particular srv socket (address:port)
s.listen(5)                                                        # length of queue for connections waiting to be accept()-ed
print 'My PID is: ' + str(os.getpid())                             # whoami for debugging purposes

def client_thread(connection):
    while True:
        tic = time.time()
        readbuf = connection.recv(1024)                            # reads up to a specified number of bytes of data
#        print readbuf

        workercommand = workerfulpat + ' ' + readbuf

        process = subprocess.Popen(workercommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        print output + ' LISTENER'

        connection.send('Rcvd ' + str(len(readbuf)) + ' bytes ' + output + str(error))    # sending a response
#        print readbuf + ' and I needed ' + str (time.time()-tic) + ' seconds.'
#        if 'end' in readbuf: break
        if not('continue' in readbuf): break
    connection.close()

while True:                                                        # loop for listening
    connection, address = s.accept()
    thread.start_new_thread(client_thread,(connection,))

s.shutdown(socket.SHUT_RDWR)
s.close()
print 'Bye bye.'

