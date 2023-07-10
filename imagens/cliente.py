import socket

hostname = socket.gethostname()
ip_Adress = socket.gethostbyname(hostname)
host = ip_Adress
port = 7002

buffer_size = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('Conexão estabelecida com o servidor.')

tamanho_arquivo = int(client_socket.recv(1024).decode())   
with open('video.avi', 'wb') as video_file:
    bytes_recebidos = 0
    while bytes_recebidos < tamanho_arquivo:
        data = client_socket.recv(4096)
        bytes_recebidos += len(data)
        video_file.write(data)   
print('Vídeo recebido e salvo com sucesso!')
