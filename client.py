# Import socket module
import socket
import time

port = 65432
addr = '172.26.204.205' # '127.0.0.1'

def sendBadgeInfo (badgeID):
    s = socket.socket()
    s.connect((addr, port))
    s.send(badgeID)
    print "sent badge ID {}".format(badgeID)
    s.close()

while True:
    sendBadgeInfo('876543')
    time.sleep(3)
# # close the connection
# s.close()
