import socket
<<<<<<< HEAD
 
 
ip = '10.0.0.182'
port = 7000
# ip = 'localhost'
# port = 5000
addr = ((ip, port))
=======
ip = input("Digite o IP do servidor: ")
port = 7017
nome = input("Digite seu nome: ")
addr = ((ip,port))
>>>>>>> 6aca37cb3bd764d444adbc8f84c68a7f921474ec
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
client_socket.send(nome.encode())
while True:
    mensagem = input("Digite a mensagem: ")
    client_socket.send(mensagem.encode())
    if mensagem == 'bye':
        client_socket.send(mensagem.encode())
        recv_msg = client_socket.recv(1024)
        if recv_msg.decode() == 'bye':
            client_socket.close()
            print("Conexão finalizada")
            break
