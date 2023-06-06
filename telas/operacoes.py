import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pooII" 
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM cadastro")
resultado = cursor.fetchall()
for x in resultado:
    print(x)

#cursor.execute("DROP TABLE IF EXISTS cadastro")
#cursor.execute("DELETE FROM cadastro")

class Operacoes():
    def __init__(self):
        cursor.execute("""CREATE TABLE cadastro (
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
        cursor.execute('''INSERT INTO cadastro (nome, email, endereco, nascimento, usuario, senha, confirmar_senha, plano_assinatura) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', (pessoa.nome, pessoa.email, pessoa.endereco, pessoa.nascimento, pessoa.usuario, pessoa.senha, pessoa.confirmar_senha, pessoa.plano_assinatura))
        conexao.commit()
        return True

    def verificar_login(self, username, password):
        if self.username == 'admin' and self.password == 'admin':
            return True
        else:
            return False
    def verificar_usuario_existente(usuario):
        cursor.execute("SELECT * FROM cadastro WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()
        if resultado:
            print("O usuário existe.")
        else:
            print("O usuário não existe.")


