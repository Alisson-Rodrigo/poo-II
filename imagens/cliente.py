import socket

# Configurações do cliente
host = '192.168.1.112'
port = 7001

# Tamanho do buffer para leitura e recebimento dos dados
buffer_size = 4096

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('Conexão estabelecida com o servidor.')

# Abre o arquivo para salvar o vídeo recebido
video_file = open('filme.mp4', 'wb')

# Recebe os pacotes de dados do servidor e escreve no arquivo
while True:
    # Recebe os dados do servidor
    data = client_socket.recv(buffer_size)
    if not data:
        # Fim da transmissão
        break
    # Escreve os dados no arquivo
    video_file.write(data)

# Fecha o arquivo e o socket
video_file.close()
client_socket.close()
