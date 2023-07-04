import socket, time
 
 
ip = '10.180.42.115'
port = 6500
name = input("Digite seu nome: ")
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
client_socket.send(name.encode())
msg = input('Digite sua mensagem: ')
client_socket.send(msg.encode())
while msg != 'bye':
    msg = input()
    client_socket.send(msg.encode())
client_socket.close()