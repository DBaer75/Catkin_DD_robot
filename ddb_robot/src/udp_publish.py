import socket
import rospy


#UDP IP and PORT
UDP_IP = "127.0.0.1" #home apartment building
UDP_PORT = 5005 #home apt




#UDP MESSAGE COMPONENTS
HEAD = "RBT"
MSG_TYPE = "GET"
MSG_TYPE = "ACK"
MSG_TYPE = "SET"
SEP = " "
DATA_TYPE = "VEL"
DATA_TYPE = "POS"
#DATA is n length char
#TAIL is 1 char checksum

#RBT SET VEL DATA TAIL

VERSION = 2
rospy.init_node('time_node')
rate = rospy.Rate(10)

def createChecksum(buff):
    r = 0
    for i in range(len(buff)):
        r = VERSION*(r+ord(buff[i]))
        #print(r)
    r = r & 0xff
    #print(r)
    #print(chr(r))
    return chr(r)

def buildUDPFromInputs():
    HEAD = "RBT"
    SEP = " "
    MSG_TYPE = raw_input("Enter MSG TYPE (SET):")#GET and ACK to be implemented later
    COMMAND = raw_input("Enter COMMAND (VEL):") #pos not implemented yet
    DATA0 = raw_input("Enter left wheel velocity(rad/s)")
    DATA1 = raw_input("Enter right wheel velocity(rad/s)")

    buff = HEAD + SEP 
    buff = buff + MSG_TYPE + SEP
    buff = buff + COMMAND + SEP
    buff = buff + DATA0 + SEP + DATA1 + SEP
    buff = buff + createChecksum(buff)
    return buff 


MESSAGE = buildUDPFromInputs()

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE


while True:
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    rate.sleep()
