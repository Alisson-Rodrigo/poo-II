import socket

host = '10.180.44.22'
port = 7002

buffer_size = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('Conexão estabelecida com o servidor.')

video_file = open('filme.mp4', 'wb')

while True:
    data = client_socket.recv(buffer_size)
    if not data:
        break
<<<<<<< HEAD
    # Escreve os dados no arquivo
=======
    print (data)
>>>>>>> 6d42d63f91a378ce3b755254b5c8ff7e10dea8bd
    video_file.write(data)
# Fecha o arquivo e o socket
video_file.close()
client_socket.close()
