import mysql.connector
import threading, socket
import os
import time

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Curupira098*",
    #linux: Curupira098*
    database="bdPOO" 
)

cursor = conexao.cursor()

class Operacoes():
    def __init__(self):

        cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            email VARCHAR(50),
            endereco VARCHAR(50),
            nascimento VARCHAR(50),
            usuario VARCHAR(50),
            senha VARCHAR(50),
            confirmar_senha VARCHAR(50)
        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS generos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50)
        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS diretores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50)
        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS filmes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(100),
            caminho VARCHAR(60),
            ano INT,
            usuario_id INT,
            genero_id INT,
            diretor_id INT,
            FOREIGN KEY (usuario_id) REFERENCES cadastro (id),
            FOREIGN KEY (genero_id) REFERENCES generos (id),
            FOREIGN KEY (diretor_id) REFERENCES diretores (id)
        )""")



        conexao.commit()

    def cadastramento (self, nome, email, endereco, nascimento, usuario, senha, confirmar_senha):
        if self.verificar_usuario_existente(usuario) == True:
            return False
        else:
            cursor.execute('''INSERT INTO cadastro (nome, email, endereco, nascimento, usuario, senha, confirmar_senha) VALUES (%s,%s,%s,%s,%s,%s,%s)''', (nome, email, endereco, nascimento, usuario, senha, confirmar_senha))
            conexao.commit()
            return True

    def verificar_login(self, username, password):
        self.verificacao = self.verificar_usuario_existente(username)
        if self.verificacao == True:
            cursor.execute("SELECT * FROM cadastro WHERE usuario = %s AND senha = %s", (username, password))
            resultado = cursor.fetchall()
            if resultado:
                return True
            else:
                return False
        else:
            return False

    def verificar_usuario_existente(self,usuario):
        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchall()
        if resultado:
            return True
        return False

    def exibir_dados(self,usuario):
        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchall()
        return resultado
    

class MyThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.name = ''
        self.client_socket = client_socket
        print('Nova conexão, endereço: ', client_address)
 
    def run(self):
        con = self.client_socket
        while True:
            try:
                mensagem = con.recv(1024)
                mensagem_str = mensagem.decode().split(',')
                if mensagem_str[0] == '1':
                    email = mensagem_str[1]
                    senha = mensagem_str[2]
                    enviar = ''
                    if sistema.verificar_login(email, senha):
                        enviar = '1'
                    else:
                        enviar = '0'
                    con.send(enviar.encode())
                elif mensagem_str[0] == '2':
                    nome = mensagem_str[1]
                    email = mensagem_str[2]
                    endereco = mensagem_str[3]
                    nascimento = mensagem_str[4]
                    usuario = mensagem_str[5]
                    senha = mensagem_str[6]
                    confirmar_senha = mensagem_str[7]
                    enviar = ''
                    if sistema.cadastramento(nome, email, endereco, nascimento, usuario, senha, confirmar_senha):
                        enviar = '1'
                    else:
                        enviar = '0'
                    con.send(enviar.encode())
                elif mensagem_str[0] == '3':
                    username = mensagem_str[1]
                    dados = f'{sistema.exibir_dados(username)}'
                    con.send(dados.encode())
                elif mensagem_str[0] == '4':
                    caminho = mensagem_str[1]
                    print(caminho)
                    self.enviar_filme(caminho)
            except ConnectionResetError:
                print('A conexão foi redefinida pelo cliente.')
                con.close()
            except Exception as e:
                print(str(e))
                con.close()
                break

    def enviar_filme(self,caminho):
        buffer_size = 4096
        video_file_path = f'/home/purehito/Documentos/GitHub/poo-II/sistema/videos/{caminho}'
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

if __name__ == "__main__":
    sistema = Operacoes()
    hostname = socket.gethostname()
    ip_Adress = socket.gethostbyname(hostname)
    ip = '10.0.0.176'
    port = 10006
    addr = ((ip, port))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    print('Aguardando conexão...')
    while True:
        server_socket.listen(10)
        client_socket, addr = server_socket.accept()
        my_thread = MyThread(addr, client_socket)
        my_thread.start()

