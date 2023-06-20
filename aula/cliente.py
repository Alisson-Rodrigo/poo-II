import socket

host = '10.180.46.41'
port = 8089
addr = (host, port)
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(addr)

while True:
    try:
        mensagem = input('digite a mensagem: ')
        cliente_socket.send(mensagem.encode())
        print ('aguardando mensagem')
        mensagem_recebida = cliente_socket.recv(1024).decode()
        if mensagem == 'sair':
            print ('conexao fechada')
            cliente_socket.close()
            break
        if mensagem_recebida == 'sair':
            print ('conexao fechada')
            cliente_socket.close()
            break
        print (f'mensagem recebida: {mensagem_recebida}')
    except:
        cliente_socket.close()
        break	