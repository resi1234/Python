#/usr/bin/python3
import socket
#where to send data
target_ip="13.82.4.173"
target_port=8888
#                  ipv4         udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4 > 3 :
    #now generating message to sender
    msg=input("plz enter your message  :  ")
    #converting data to ascii
    n=msg.encode('ascii')
    s.sendto(n,(target_ip,target_port))
    #rec from sender
    print(s.recvfrom(100))
    
