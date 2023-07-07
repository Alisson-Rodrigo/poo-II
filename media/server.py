import socket
import os
hostname = socket.gethostname()
ip_Adress = socket.gethostbyname(hostname)
host = ip_Adress
port = 7002

buffer_size = 4096

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print('Aguardando conexão...')

client_socket, addr = server_socket.accept()
print('Conexão estabelecida com:', addr)

buffer_size = 4096
video_file_path = 'videoplayback.avi'
video_file_size = os.path.getsize(video_file_path)       
with open(video_file_path, 'rb') as video_file:
    client_socket.send(str(video_file_size).encode())            
    while True:
        data = video_file.read(buffer_size)
        if not data:
            break
        client_socket.send(data)
        print (data)

# Fecha o arquivo e o socket
video_file.close()
client_socket.close()
server_socket.close()
