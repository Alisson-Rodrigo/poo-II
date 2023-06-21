import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
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
            endereco VARCHAR(100),
            nascimento varchar(20),
            usuario VARCHAR(20),
            senha VARCHAR(20),
            confirmar_senha VARCHAR(20),
            plano_assinatura VARCHAR(40)
        )""")
        conexao.commit()

    def cadastramento (self, pessoa):
        if self.verificar_usuario_existente(pessoa.usuario) == True:
            return False
        else:
            cursor.execute('''INSERT INTO cadastro (nome, email, endereco, nascimento, usuario, senha, confirmar_senha, plano_assinatura) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', (pessoa.nome, pessoa.email, pessoa.endereco, pessoa.nascimento, pessoa.usuario, pessoa.senha, pessoa.confirmar_senha, pessoa.plano_assinatura))
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
    


if __name__ == "__main__":
    import socket

    sistema = Operacoes()
    host = '10.0.0.184'
    port = 5000
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
                    print(f'Usuário {email} efetuou o login no sistema')
                else:
                    enviar = '0'
                    print('Erro no login')
                con.send(enviar.encode())
            elif mensagem_str[0] == '2':
                pass
            elif mensagem_str[0] == '0':
                pass
            else:
                raise Exception('Conexão finalizada pelo cliente')
        except Exception as e:
            print(str(e))
            con.close()
            serv_socket.close()
            break


