import socket

host = '10.180.44.22'
port = 7001

buffer_size = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('Conexão estabelecida com o servidor.')

video_file = open('filme.mp4', 'wb')

while True:
    data = client_socket.recv(buffer_size)
    if not data:
        break
    print (data)
    video_file.write(data)
# Fecha o arquivo e o socket
video_file.close()
client_socket.close()
