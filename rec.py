#!/usr/bin/python3
import socket
ip="0.0.0.0" # 1024 --65535 free range of port
port=8888  #generate type of socket

#generate protocol type of socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # udp docket created

#to bind i can combine ip and port

s.bind((ip,port))
while True:
    web=s.recvfrom(100)
    print(web) 
 #reply to sender
    s.sendto("okay".encode('ascii'))
    

