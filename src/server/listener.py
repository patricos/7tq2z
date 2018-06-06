# Server program for RPN expression calculator
# by Patryk Mazurkiewicz in Jun 2018
#
# OKAY: listens
# todo: properly shut the socket disused
# todo: parses input
# todo: registers timings
# todo: logs timings and necessary things
# todo: spawns workers
# todo: receives results from worker
# OKAY: sends results back

import socket

serveripaddr = 'localhost'
serveripport = 8088

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # creates socket object of AF_INET family and SOCK_STREAM type
serversocket.bind((serveripaddr, serveripport))                    # configs the socket for a particular srv socket (address:port)
serversocket.listen(7)                                         	   # opens up a socket for at most 7 connections

while True:                                                        # loop for "always listenineg"
    connection, address = serversocket.accept()
    readbuf = connection.recv(255)                                 # reads up to 255 characters of data

    while len(readbuf) > 0:

        # input data processing block
        print readbuf
        connection.send('Rcvd ' + str(len(readbuf)) + ' bytes')    # sending a response
        if readbuf == 'exit':                                      # eventually exiting when asked to
	        break
        else:
            readbuf = connection.recv(255)                         # reads up to 255 characters of data

    if readbuf == 'exit':                                          # eventually exiting when asked to
        connection.close()
        break

