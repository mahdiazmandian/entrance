# Import socket module
import socket
import time

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

while True:

    s.send("Badge Number: 123456")
    print "sent message"
    time.sleep(3)
# # close the connection
# s.close()