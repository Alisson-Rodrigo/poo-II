import mysql.connector
import threading
import socket
import os

# Estabelece a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bdPOO"
)

cursor = conexao.cursor()

class Operacoes:
    """
    Classe que define as operações relacionadas ao banco de dados.
    """

    def __init__(self):
        """
        Inicializa a classe Operacoes.
        Cria as tabelas 'cadastro' e 'filmes', se não existirem.
        """
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

        cursor.execute("""CREATE TABLE IF NOT EXISTS filmes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            caminho VARCHAR(200),
            genero VARCHAR(50),
            diretor VARCHAR(50)
        )""")

        conexao.commit()

    def cadastramento(self, nome, email, endereco, nascimento, usuario, senha, confirmar_senha):
        """
        Realiza o cadastro de um novo usuário.

        Args:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
            endereco (str): O endereço do usuário.
            nascimento (str): A data de nascimento do usuário.
            usuario (str): O nome de usuário escolhido pelo usuário.
            senha (str): A senha escolhida pelo usuário.
            confirmar_senha (str): A confirmação da senha escolhida pelo usuário.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        if self.verificar_usuario_existente(usuario):
            return False
        else:
            cursor.execute('''INSERT INTO cadastro (nome, email, endereco, nascimento, usuario, senha, confirmar_senha) VALUES (%s,%s,%s,%s,%s,%s,%s)''', (nome, email, endereco, nascimento, usuario, senha, confirmar_senha))
            conexao.commit()
            return True

    def verificar_login(self, username, password):
        """
        Verifica se as credenciais de login são válidas.

        Args:
            username (str): O nome de usuário.
            password (str): A senha do usuário.

        Returns:
            bool: True se as credenciais forem válidas, False caso contrário.
        """
        self.verificacao = self.verificar_usuario_existente(username)
        if self.verificacao:
            cursor.execute("SELECT * FROM cadastro WHERE usuario = %s AND senha = %s", (username, password))
            resultado = cursor.fetchall()
            if resultado:
                return True
            else:
                return False
        else:
            return False

    def verificar_usuario_existente(self, usuario):
        """
        Verifica se um usuário já existe no banco de dados.

        Args:
            usuario (str): O nome de usuário a ser verificado.

        Returns:
            bool: True se o usuário existir, False caso contrário.
        """
        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchall()
        if resultado:
            return True
        return False

    def exibir_dados(self, usuario):
        """
        Retorna os dados de um usuário específico.

        Args:
            usuario (str): O nome de usuário.

        Returns:
            list: Uma lista contendo os dados do usuário.
        """
        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchall()
        return resultado

    def exibir_dadosADMIN(self):
        """
        Retorna os nomes de todos os usuários registrados no banco de dados.

        Returns:
            list: Uma lista contendo os nomes de usuário.
        """
        cursor.execute("SELECT usuario FROM cadastro")
        resultados = cursor.fetchall()
        nomes = [resultado[0] for resultado in resultados]
        return nomes

    def deletar_usuario(self, usuario):
        """
        Deleta um usuário específico do banco de dados.

        Args:
            usuario (str): O nome de usuário a ser excluído.

        Returns:
            bool: True se o usuário for excluído com sucesso, False caso contrário.
        """
        cursor.execute("DELETE FROM cadastro WHERE usuario = %s", (usuario,))
        conexao.commit()
        return True

    def verificar_midia_existente(self, nome_filme, caminho):
        """
        Verifica se uma mídia já existe no banco de dados.

        Args:
            nome_filme (str): O nome do filme.
            caminho (str): O caminho do filme.

        Returns:
            bool: True se a mídia não existir, False caso contrário.
        """
        cursor.execute("SELECT * FROM filmes WHERE nome = %s AND caminho = %s", (nome_filme, caminho))
        resultado = cursor.fetchall()
        if resultado:
            return False
        return True

    def adicionar_midia(self, nome_filme, genero, diretor, caminho):
        """
        Adiciona uma nova mídia ao banco de dados.

        Args:
            nome_filme (str): O nome do filme.
            genero (str): O gênero do filme.
            diretor (str): O diretor do filme.
            caminho (str): O caminho do filme.

        Returns:
            bool: True se a mídia for adicionada com sucesso, False caso contrário.
        """
        if self.verificar_midia_existente(nome_filme, caminho):
            cursor.execute("""INSERT INTO filmes (nome, genero, diretor, caminho) VALUES (%s,%s,%s,%s)""", (nome_filme, genero, diretor, caminho))
            conexao.commit()
            return True
        else:
            return False

    def exibir_filmes(self):
        """
        Retorna os dados de todos os filmes registrados no banco de dados.

        Returns:
            list: Uma lista contendo os nomes, caminhos e gêneros dos filmes.
        """
        cursor.execute("SELECT nome, caminho, genero FROM filmes")
        resultado = cursor.fetchall()
        return resultado

    def deletar_midia(self, nome_filme):
        """
        Deleta um filme específico do banco de dados.

        Args:
            nome_filme (str): O nome do filme a ser excluído.

        Returns:
            bool: True se o filme for excluído com sucesso, False caso contrário.
        """
        cursor.execute("DELETE FROM filmes WHERE nome = %s", (nome_filme,))
        conexao.commit()
        return True

class MyThread(threading.Thread):
    """
    Classe que lida com as conexões de cliente em threads separadas.
    """

    def __init__(self, client_address, client_socket):
        """
        Inicializa a classe MyThread.

        Args:
            client_address (tuple): O endereço do cliente.
            client_socket (socket): O socket do cliente.
        """
        threading.Thread.__init__(self)
        self.name = ''
        self.client_socket = client_socket
        print('Nova conexão, endereço: ', client_address)
        self.lock = threading.Lock()

    def run(self):
        """
        Executa a thread para lidar com as solicitações do cliente.
        """
        while True:
            con = self.client_socket
            try:
                mensagem = con.recv(1024)
                mensagem_str = mensagem.decode().split(',')
                if mensagem_str[0] == '1':
                    # Verifica o login
                    email = mensagem_str[1]
                    senha = mensagem_str[2]
                    enviar = ''
                    if sistema.verificar_login(email, senha):
                        enviar = '1'
                    else:
                        enviar = '0'
                    con.send(enviar.encode())
                elif mensagem_str[0] == '2':
                    # Realiza o cadastro de um novo usuário
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
                    # Exibe os dados de um usuário específico
                    username = mensagem_str[1]
                    dados = f'{sistema.exibir_dados(username)}'
                    con.send(dados.encode())
                elif mensagem_str[0] == '4':
                    # Envia um filme para o cliente
                    caminho = mensagem_str[1]
                    self.enviar_filme(caminho, con)
                elif mensagem_str[0] == '5':
                    # Libera um recurso
                    self.lock
                    self.lock.acquire()
                    try:
                        enviar = 'liberado'
                        con.send(enviar.encode())
                    finally:
                        self.lock.release()
                elif mensagem_str[0] == '6':
                    enviar = ''
                    if mensagem_str[1] == 'exibir_usuarios':
                        # Exibe os usuários registrados no banco de dados
                        exibir_dadosADMIN = sistema.exibir_dadosADMIN()
                        enviar = exibir_dadosADMIN
                    elif mensagem_str[1] == 'deletar_usuario':
                        # Deleta um usuário do banco de dados
                        usuario = mensagem_str[2]
                        if sistema.deletar_usuario(usuario):
                            enviar = '1'
                        else:
                            enviar = '0'
                    elif mensagem_str[1] == 'adicionar_midia':
                        # Adiciona uma mídia ao banco de dados
                        nome_filme = mensagem_str[2]
                        genero = mensagem_str[3]
                        diretor = mensagem_str[4]
                        caminho = mensagem_str[5]
                        if sistema.adicionar_midia(nome_filme, genero, diretor, caminho):
                            enviar = '1'
                        else:
                            enviar = '0'
                    elif mensagem_str[1] == 'deletar_midia':
                        # Deleta uma mídia do banco de dados
                        nome_filme = mensagem_str[2]
                        if sistema.deletar_midia(nome_filme):
                            enviar = '1'
                        else:
                            enviar = '0'
                    elif mensagem_str[1] == 'exibir_todos_filmes':
                        # Exibe todas as mídias registradas no banco de dados
                        enviar = sistema.exibir_filmes()
                    con.send(str(enviar).encode())

            except ConnectionResetError:
                print('A conexão foi redefinida pelo cliente.')
                con.close()
            except Exception as e:
                print(str(e))
                con.close()
                break

    def enviar_filme(self, caminho, client_socket):
        """
        Envia um arquivo de vídeo para o cliente.

        Args:
            caminho (str): O caminho do arquivo de vídeo.
            client_socket (socket): O socket do cliente.
        """
        buffer_size = 4096
        video_file_path = f'C:/Users/PurooLight/Documents/estudos/pooII/poo-II/sistema/videos/{caminho}'
        if os.path.exists(video_file_path):
            video_file_size = os.path.getsize(video_file_path)
            with open(video_file_path, 'rb') as video_file:
                client_socket.send(str(video_file_size).encode())
                while True:
                    data = video_file.read(buffer_size)
                    if not data:
                        break
                    client_socket.send(data)
            video_file.close()
            print('Arquivo enviado com sucesso.')
        else:
            client_socket.send(str(0).encode())
            print('Arquivo não encontrado no servidor.')

if __name__ == "__main__":
    sistema = Operacoes()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip = '10.0.0.176'
    port = 10010
    addr = (ip, port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    print('Aguardando conexão...')
    while True:
        server_socket.listen(10)
        client_socket, addr = server_socket.accept()
        my_thread = MyThread(addr, client_socket)
        my_thread.start()
