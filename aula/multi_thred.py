import socket

host = 'localhost'
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print ('aguardando conexao')
con, cliente = serv_socket.accept()
print ('conectado')
print ('aguardando mensagem')

while True:
    try:
        recebe = con.recv(1024)
        if recebe == 'sair':
            print ('desconectado')
            serv_socket.close()
            break
        print ('mensagem recebida: ', recebe.decode())
        enviar = input('digite a mensagem: ')
        con.send(enviar.encode())
        
    except Exception as erro:
        print (str(erro))
        serv_socket.close()
        break
