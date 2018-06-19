# Server program for RPN expression calculator
# by Patryk Mazurkiewicz in Jun 2018
#
# OKAY: listens
# NOPE: sanitize the input (ascii, perhaps limited ser of characters)
# OKAY: properly shut the socket disused
# OKAY: parses input
# OKAY: registers timings
# OKAY: logs timings and necessary things
# OKAY: spawns workers
# OKAY: receives results from worker
# OKAY: sends results back

import socket       # s.socket, s.bind, s.listen, s.send, s.recv
import thread       # thread.start_new_thread()
import os           # os.getpid()
import time         # time.time()
import subprocess   # subprocess.Popen(), process.communicate()

serveripaddr = 'localhost'                  # = socket.gethostname()
serveripport = 8088
loggeripaddr = 'localhost'
loggeripport = 8089
workerfulpat = '../worker/rpnworker'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # creates socket object of AF_INET family and SOCK_STREAM type
s.bind((serveripaddr, serveripport))                               # configs the socket for a particular srv socket (address:port)
s.listen(5)                                                        # length of queue for connections waiting to be accept()-ed
print 'My PID is: ' + str(os.getpid())                             # whoami for debugging purposes

def client_thread(connection):
    while True:
        readbuf = connection.recv(1024)                            # reads up to a specified number of bytes of data
        workercommand = workerfulpat + ' ' + readbuf               # prepares for launching a new worker

        tic = time.time()
        process = subprocess.Popen(workercommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        toc = time.time()

        if not error is None: output = output + ' error:' + str(error)   # passing error code
        connection.send(output)                                    # sending a response to client
        
        logsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logsock.connect((loggeripaddr, loggeripport))
        tictoc = str( round(toc-tic,3) )
        logsock.send(  tictoc + ", " + readbuf  )                  # to log file:  "[time], [inputExpression]"
        logsock.close()

        if not('continue' in readbuf): break                       # future feature; all rpn-s 2 B processed w/one socket reservation
    connection.close()

while True:                                                        # loop for listening
    connection, address = s.accept()
    thread.start_new_thread(client_thread,(connection,))

s.shutdown(socket.SHUT_RDWR)
s.close()
print 'Bye bye.'

