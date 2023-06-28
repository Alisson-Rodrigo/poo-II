import mysql.connector

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
    
if __name__ == "__main__":
    import socket

    sistema = Operacoes()
    host = 'localhost'
    port = 8902
    addr = (host, port)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    print('Aguardando conexão...')
    con, cliente = serv_socket.accept()
    print('Conectado')
    print('Aguardando interação...')

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
            else:
                raise Exception('Conexão finalizada pelo cliente')
        except Exception as e:
            print(str(e))
            con.close()
            serv_socket.close()
            break


