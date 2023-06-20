import socket

class Comunicacao():
    def __init__(self):
        self.host = 'localhost'
        self.port = 9000
        self.addr = (self.host, self.port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_socket.bind(self.addr)
        self.serv_socket.listen(10)
        print ('aguardando conexao')
        self.con, cliente = self.serv_socket.accept()
        print ('conectado')
        print ('aguardando mensagem')
    def login (self):
        recebe = self.con.recv(1024)
        recebe.decode()
        print (recebe)
