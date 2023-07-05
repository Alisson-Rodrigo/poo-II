import socket

def connect_to_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Conexão estabelecida com o servidor.")

    message = input("Digite uma mensagem para enviar ao servidor: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024)
    print("Resposta do servidor:", response.decode('utf-8'))

    client_socket.close()

# Endereço IP público do servidor
server_ip = '127.0.0.1'
# Porta na qual o servidor está escutando
server_port = 8000
connect_to_server(server_ip,server_port)