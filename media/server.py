import socket

# Configurações do servidor
host = '10.0.0.182'
port = 7001

# Tamanho do buffer para leitura e envio dos dados
buffer_size = 4096

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print('Aguardando conexão...')

# Aceita a conexão do cliente
client_socket, addr = server_socket.accept()
print('Conexão estabelecida com:', addr)

# Abre o arquivo de vídeo em modo binário
video_file = open('videoplayback.avi', 'rb')

# Envia os pacotes de dados para o cliente
while True:
    # Lê o próximo bloco de dados do arquivo
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
