import socket

host = 'localhost'
port = 8000
addr = (host, port)
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(addr)

while True:
    try:
        mensagem = input('digite a mensagem: ')
        cliente_socket.send(mensagem.encode())
        print ('aguardando mensagem')
        print ('mensagem recebida: ', cliente_socket.recv(1024).decode())
    except:
        cliente_socket.close()
        break