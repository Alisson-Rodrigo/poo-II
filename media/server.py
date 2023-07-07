import socket

host = '10.180.44.22'
port = 7002

buffer_size = 4096

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print('Aguardando conexão...')

client_socket, addr = server_socket.accept()
print('Conexão estabelecida com:', addr)

video_file = open('videoplayback.avi', 'rb')

while True:
    data = video_file.read(buffer_size)
    if not data:
        # Fim do arquivo
        break
    # Envia os dados para o cliente
    client_socket.send(data)

# Fecha o arquivo e o socket
video_file.close()
client_socket.close()
server_socket.close()
