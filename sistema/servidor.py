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
    '''
    Essa classe é responsável por realizar as operações no banco de dados. Desde de cadastrar um novo usuário, verificar se o usuário existe, verificar se o login está correto, exibir os dados do usuário, adicionar uma nova mídia, exibir todas as mídias, deletar uma mídia, deletar um usuário, exibir todos os usuários.

    Parameters
    ------
    none

    Attributes
    ------
    none
    
    Methods
    ------
    cadastramento(nome, email, endereco, nascimento, usuario, senha, confirmar_senha)
        Realiza o cadastramento de um novo usuário no banco de dados.
    verificar_login(username, password)
        Verifica se o login está correto.
    verificar_usuario_existente(usuario)
        Verifica se o usuário já existe no banco de dados.
    exibir_dados(usuario)
        Exibe os dados do usuário.
    exibir_dadosADMIN()
        Exibe todos os usuários.
    deletar_usuario(usuario)
        Deleta um usuário.
    verificar_midia_existente(nome_filme, caminho)
        Verifica se a mídia já existe no banco de dados.
    adicionar_midia(nome_filme, genero, diretor, caminho)
        Adiciona uma nova mídia no banco de dados.
    exibir_filmes()
        Exibe todas as mídias.
    deletar_midia(nome_filme)
        Deleta uma mídia.
    
    return
    ------
    True
        Se a operação for realizada com sucesso.
    False
        Se a operação não for realizada com sucesso.
    '''
    def __init__(self):
        '''
        Essa função é responsável por criar as tabelas no banco de dados. Caso as tabelas já existam, não será criada uma nova tabela.

        Parameters
        ------
        none

        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        none

        '''
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

    def cadastramento (self, nome, email, endereco, nascimento, usuario, senha, confirmar_senha):
        '''
        Essa função é responsável por realizar o cadastramento de um novo usuário no banco de dados.

        Parameters
        ------
        nome : str
            Nome do usuário.
        email : str
            Email do usuário.
        endereco : str
            Endereço do usuário.
        nascimento : str
            Data de nascimento do usuário.
        usuario : str
            Nome de usuário do usuário.
        senha : str
            Senha do usuário.
        confirmar_senha : str
            Confirmação da senha do usuário.
        
        Attributes
        ------
        none

        Methods
        ------
        verificar_usuario_existente(usuario)
            Verifica se o usuário já existe no banco de dados.
        
        return
        ------
        True
            Se o usuário não existir no banco de dados e o cadastramento for realizado com sucesso.
        False
            Se o usuário já existir no banco de dados e o cadastramento não for realizado com sucesso.
        '''
        if self.verificar_usuario_existente(usuario) == True:
            return False
        else:
            cursor.execute('''INSERT INTO cadastro (nome, email, endereco, nascimento, usuario, senha, confirmar_senha) VALUES (%s,%s,%s,%s,%s,%s,%s)''', (nome, email, endereco, nascimento, usuario, senha, confirmar_senha))
            conexao.commit()
            return True

    def verificar_login(self, username, password):
        '''
        Essa função é responsável por verificar se o login está correto.

        Parameters
        ------
        username : str
            Nome de usuário do usuário.
        password : str
            Senha do usuário.

        Attributes
        ------
        none

        Methods
        ------
        verificar_usuario_existente(usuario)
            Verifica se o usuário já existe no banco de dados.
        
        return
        ------
        True
            Se o usuário existir no banco de dados e o login estiver correto.
        False
            Se o usuário não existir no banco de dados e o login não estiver correto.
        '''
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
        '''
        Essa função é responsável por verificar se o usuário já existe no banco de dados.

        Parameters
        ------
        usuario : str
            Nome de usuário do usuário.
        
        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        True
            Se o usuário existir no banco de dados.
        False
            Se o usuário não existir no banco de dados.
        '''

        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchall()
        if resultado:
            return True
        return False

    def exibir_dados(self,usuario):
        '''
        Essa função é responsável por exibir os dados do usuário.

        Parameters
        ------
        usuario : str
            Nome de usuário do usuário.
        
        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        resultado : list
            Lista com os dados do usuário.
        '''
        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchall()
        return resultado
    
    def exibir_dadosADMIN(self):
        '''
        Essa função é responsável por exibir todos os usuários.

        Parameters
        ------
        none

        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        nomes : list
            Lista com todos os usuários.
        
        '''
        cursor.execute("SELECT usuario FROM cadastro")
        resultados = cursor.fetchall()
        nomes = [resultado[0] for resultado in resultados] 
        return nomes
    def deletar_usuario(self,usuario):
        '''
        Essa função é responsável por deletar um usuário.

        Parameters
        ------
        usuario : str
            Nome de usuário do usuário.
        
        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        True
            Se o usuário for deletado com sucesso.
        False
            Se o usuário não for deletado com sucesso.
        
        '''
        cursor.execute("DELETE FROM cadastro WHERE usuario = %s", (usuario,))
        conexao.commit()
        return True
    
    def verificar_midia_existente(self, nome_filme, caminho):
        '''
        Essa função é responsável por verificar se a mídia já existe no banco de dados.

        Parameters
        ------
        nome_filme : str
            Nome da mídia.
        caminho : str
            Caminho da mídia.

        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        True
        '''
        cursor.execute("SELECT * FROM filmes WHERE nome = %s AND caminho = %s", (nome_filme, caminho))
        resultado = cursor.fetchall()
        if resultado:
            return False
        return True

    def adicionar_midia(self, nome_filme, genero, diretor, caminho):
        '''
        Essa função é responsável por adicionar uma nova mídia no banco de dados.

        Parameters
        ------
        nome_filme : str
            Nome da mídia.
        genero : str
            Gênero da mídia.
        diretor : str
            Diretor da mídia.
        caminho : str
            Caminho da mídia.

        Attributes
        ------
        none

        Methods

        return
        ------
        True
            Se a mídia não existir no banco de dados e a mídia for adicionada com sucesso.
        False
            Se a mídia existir no banco de dados e a mídia não for adicionada com sucesso.
        '''
        if self.verificar_midia_existente(nome_filme, caminho) == True:
            cursor.execute("""INSERT INTO filmes (nome, genero, diretor, caminho) VALUES (%s,%s,%s,%s)""", (nome_filme, genero, diretor, caminho))
            conexao.commit()
            return True
        else:
            return False
    def exibir_filmes(self):
        '''
        Essa função é responsável por exibir todas as mídias.

        Parameters
        ------
        none

        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        resultado : list
            Lista com todas as mídias.

        '''
        cursor.execute("SELECT nome, caminho, genero FROM filmes")
        resultado = cursor.fetchall()
        return resultado
    

    def deletar_midia(self, nome_filme):
        '''
        Essa função é responsável por deletar uma mídia.

        Parameters
        ------
        nome_filme : str
            Nome da mídia.
        
        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        True
            Se a mídia for deletada com sucesso.
        False
            Se a mídia não for deletada com sucesso.

        '''
        cursor.execute("DELETE FROM filmes WHERE nome = %s", (nome_filme,))
        conexao.commit()
        return True

class MyThread(threading.Thread):
    '''
    Essa classe é responsável por criar uma nova thread para cada cliente que se conectar ao servidor.
    Com isso, o servidor pode atender vários clientes ao mesmo tempo.

    Parameters
    ------
    client_address : str
        Endereço do cliente.
    client_socket : str
        Socket do cliente.
    
    Attributes
    ------
    name : str
        Nome da thread.
    client_socket : str
        Socket do cliente.
    lock : str
        Lock para controlar o acesso ao recurso compartilhado.
    
    Methods
    ------
    run()
        Inicia a thread.
    enviar_filme(caminho, client_socket)
        Envia o filme para o cliente.
    
    return
    ------
    none
    '''
    def __init__(self, client_address, client_socket):
        '''
        Essa função de inicialização é responsável por criar uma nova thread para cada cliente que se conectar ao servidor.

        Parameters
        ------
        client_address : str
            Endereço do cliente.
        client_socket : str
            Socket do cliente.
        
        Attributes
        ------
        name : str
            Nome da thread.
        client_socket : str
            Socket do cliente.
        lock : str
            Lock para controlar o acesso ao recurso compartilhado.
        
        Methods
        ------
        none

        return
        ------
        none
        '''
        threading.Thread.__init__(self)
        self.name = ''
        self.client_socket = client_socket
        print('Nova conexão, endereço: ', client_address)
        self.lock = threading.Lock()

 
    def run(self):
        '''
        Essa função é responsável por iniciar a thread.
        E realizar as operações de acordo com a mensagem recebida do cliente.

        Parameters
        ------
        none

        Attributes
        ------
        none

        Methods
        ------
        enviar_filme(caminho, client_socket)
            Envia o filme para o cliente.
        verificar_login(email, senha)
            Verifica se o login está correto.
        cadastramento(nome, email, endereco, nascimento, usuario, senha, confirmar_senha)
            Realiza o cadastramento de um novo usuário no banco de dados.
        exibir_dados(usuario)
            Exibe os dados do usuário.
        deletar_usuario(usuario)
            Deleta um usuário.
        adicionar_midia(nome_filme, genero, diretor, caminho)
            Adiciona uma nova mídia no banco de dados.
        exibir_filmes()
            Exibe todas as mídias. 
        deletar_midia(nome_filme)
            Deleta uma mídia.
        exibir_dadosADMIN()
            Exibe todos os usuários.

        Exceptions
        ------
        ConnectionResetError
            Se a conexão for redefinida pelo cliente.
        Exception
            Se ocorrer algum erro.
        return
        ------
        none

        '''
        while True:
            con = self.client_socket
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
                    self.enviar_filme(caminho, con)
                elif mensagem_str[0] == '5':
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
                        exibir_dadosADMIN = sistema.exibir_dadosADMIN()
                        enviar = exibir_dadosADMIN
                    elif mensagem_str[1] == 'deletar_usuario':
                        usuario = mensagem_str[2]
                        if sistema.deletar_usuario(usuario):
                            enviar = '1'
                        else:
                            enviar = '0'
                    elif mensagem_str[1] == 'adicionar_midia':
                        nome_filme = mensagem_str[2]
                        genero = mensagem_str[3]
                        diretor = mensagem_str[4]
                        caminho = mensagem_str[5]
                        if sistema.adicionar_midia(nome_filme, genero, diretor, caminho):
                            enviar = '1'
                        else:
                            enviar = '0'
                    elif mensagem_str[1] == 'deletar_midia':
                        nome_filme = mensagem_str[2]
                        if sistema.deletar_midia(nome_filme):
                            enviar = '1'
                        else:
                            enviar = '0'
                    elif mensagem_str[1] == 'exibir_todos_filmes':
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
        '''
        Essa função é responsável por enviar o filme para o cliente.

        Parameters
        ------
        caminho : str
            Caminho do filme.
        client_socket : str
            Socket do cliente.

        Attributes
        ------
        none

        Methods
        ------
        none

        return
        ------
        none
        '''
        buffer_size = 4096
        video_file_path = f'/home/purehito/Documentos/GitHub/poo-II/sistema/videos/{caminho}'
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
    ip_Adress = socket.gethostbyname(hostname)
    ip = '10.180.46.76'
    port = 10010
    addr = ((ip, port))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    print('Aguardando conexão...')
    while True:
        server_socket.listen(10)
        client_socket, addr = server_socket.accept()
        my_thread = MyThread(addr, client_socket)
        my_thread.start()

