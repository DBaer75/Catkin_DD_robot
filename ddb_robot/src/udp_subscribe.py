import socket
import rospy


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

VERSION = 2

def checkChecksum(buff):
    r = 0
    for i in range(len(buff)-1):
        r = VERSION*(r+ord(buff[i]))
    r = r & 0xff
    return r

def decodeUDP(buff):
    data_chunk = buff.split(" ")
    for i in data_chunk:
        print i
    return data_chunk

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    decodeUDP(data)
    check_sum_should_be = checkChecksum(data)
    check_sum_rec = ord(data[len(data) - 1 ])
    if (check_sum_rec == check_sum_should_be):
        print "DATA is VALID"
    else:
        print "DATA is not VALID"

