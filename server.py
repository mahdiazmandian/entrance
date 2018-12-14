# first of all import the socket library
import socket, time
from threading import Thread

def badge_listen():

    # next create a socket object
    s = socket.socket()
    #~ s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #~ s.setsockopt(socket.SOL_SOCKET, 25, 'wlan0')
    
    print "Socket successfully created"

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 65432

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    #~ s.bind(('172.26.204.205', port))
    #~ s.bind(('wlan0', port))
    print "socket binded to %s" % (port)

    # put the socket into listening mode
    s.listen(5)
    print "socket is listening"

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print 'Got connection from', addr

        try:
            data = c.recv(1024)
            print data
        except:
            print "client left"
            break
        # # Close the connection with the client
        c.close()


counter = 0

Thread(target=badge_listen, args=()).start()

while True:
    print counter
    time.sleep(1)
    counter = counter + 1
