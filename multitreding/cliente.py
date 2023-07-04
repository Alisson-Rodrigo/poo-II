import socket
 
 
ip = '10.0.0.182'
port = 7000
# ip = 'localhost'
# port = 5000
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
 
while True:
    try:
        mensagem = input('Digite a mensagem: ')
        client_socket.send(mensagem.encode())
        
        if mensagem == 'quit':
            raise Exception('Conexão finalizada pelo cliente')
        
        print('Mensagem enviada')
        print('Mensaem recebida: ', client_socket.recv(1024).decode())
    except Exception as e:
        print(str(e))
        client_socket.close()
        break