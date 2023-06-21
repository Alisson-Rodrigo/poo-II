import mysql.connector as mysql
from modelos import Professor, Aluno


tabelas = {}
tabelas['usuarios'] = (
    "CREATE TABLE IF NOT EXISTS sistema_educacional.usuarios ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "email VARCHAR(255) NOT NULL,"
    "senha VARCHAR(255) NOT NULL,"
    "nome VARCHAR(255) NOT NULL,"
    "sobrenome VARCHAR(255) NOT NULL,"
    "nascimento DATE NOT NULL,"
    "UNIQUE (email)"
    ")"
)
tabelas['professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'salario DECIMAL(10,2) NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id)'
    ')'
)
tabelas['alunos'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.alunos ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'pontuacao_geral INT NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id)'
    ')'
)
tabelas['materias'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.materias ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'descricao VARCHAR(255) NOT NULL,'
    'professor_id INT NOT NULL,'
    'FOREIGN KEY (professor_id) REFERENCES professores(id)'
    ')'
)
tabelas['turmas'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.turmas ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'materias_id INT NOT NULL,'
    'alunos_id INT NOT NULL,'
    'nome VARCHAR(255) NOT NULL,'
    'pontuacao INT NOT NULL,'
    'FOREIGN KEY (materias_id) REFERENCES materias(id),'
    'FOREIGN KEY (alunos_id) REFERENCES alunos(id)'
    ')'
)
tabelas['atividades'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.atividades ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'descricao VARCHAR(255) NOT NULL,'
    'materia_id INT NOT NULL,'
    'FOREIGN KEY (materia_id) REFERENCES materias(id)'
    ')'
)
tabelas['questoes'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.questoes ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'enunciado VARCHAR(255) NOT NULL,'
    'resposta VARCHAR(255) NOT NULL,'
    'atividade_id INT NOT NULL,'
    'FOREIGN KEY (atividade_id) REFERENCES atividades(id)'
    ')'
)


class SistemaEducacional:
    def __init__(self):
        self._usuario = None
        self._mydb = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            auth_plugin='mysql_native_password'
        )
        self._cursor = self._mydb.cursor()
        self._sql = "CREATE DATABASE IF NOT EXISTS sistema_educacional"
        self._val = ()
        self._cursor.execute(self._sql)

        for tabela in tabelas:
            self._cursor.execute(tabelas[tabela])

        self._mydb.commit()

    @property
    def usuario(self):
        return self._usuario

    @property
    def materias(self):
        self._sql = "SELECT * FROM sistema_educacional.materias"
        self._val = ()
        self._cursor.execute(self._sql, self._val)
        return [(x[1], x[3]) for x in self._cursor.fetchall()]

    @property
    def turmas(self):
        self._sql = 'SELECT sistema_educacional.materias.nome, sistema_educacional.alunos.id \
            FROM sistema_educacional.materias \
            JOIN sistema_educacional.turmas ON sistema_educacional.materias.id = sistema_educacional.turmas.materias_id \
            JOIN sistema_educacional.alunos ON sistema_educacional.turmas.alunos_id = sistema_educacional.alunos.id'
        self._val = ()
        self._cursor.execute(self._sql, self._val)
        return self._cursor.fetchall()

    def cadastrar_professor(self, email, senha, nome, sobrenome, nascimento):
        if self.buscar(email):
            return False
        self._sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento) VALUES (%s, %s, %s, %s, %s)"
        self._val = (email, senha, nome, sobrenome, nascimento)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        professor = Professor(email, senha, nome, sobrenome, nascimento)
        professor.id = self._cursor.lastrowid
        self._usuario = professor

        self._sql = "INSERT INTO sistema_educacional.professores (usuario_id, salario) VALUES (%s, %s)"
        self._val = (professor.id, 1320)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        return True

    def cadastrar_aluno(self, email, senha, nome, sobrenome, nascimento):
        if self.buscar(email):
            return False
        self._sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento) VALUES (%s, %s, %s, %s, %s)"
        self._val = (email, senha, nome,
                     sobrenome, nascimento)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        aluno = Aluno(email, senha, nome, sobrenome, nascimento)
        aluno.id = self._cursor.lastrowid
        self._usuario = aluno

        self._sql = "INSERT INTO sistema_educacional.alunos (usuario_id, pontuacao_geral) VALUES (%s, %s)"
        self._val = (aluno.id, 0)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        return True

    def buscar(self, email):
        self._sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s"
        self._val = (email,)
        self._cursor.execute(self._sql, self._val)
        try:
            return self._cursor.fetchone()
        except:
            return False

    def autenticar(self, email, senha):
        self._sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s AND senha = %s"
        self._val = (email, senha)
        self._cursor.execute(self._sql, self._val)
        try:
            return self._cursor.fetchone()
        except:
            return False

    def login(self, email, senha):
        usuario = self.autenticar(email, senha)
        if usuario:
            self._sql = "SELECT * FROM sistema_educacional.professores WHERE usuario_id = %s"
            self._val = (usuario[0],)
            self._cursor.execute(self._sql, self._val)
            consulta = self._cursor.fetchone()
            if consulta:
                professor = Professor(
                    usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]
                )
                professor.id = consulta[0]
                self._usuario = professor
                return True
            else:
                self._sql = "SELECT * FROM sistema_educacional.alunos WHERE usuario_id = %s"
                self._val = (usuario[0],)
                self._cursor.execute(self._sql, self._val)
                consulta = self._cursor.fetchone()
                if consulta:
                    aluno = Aluno(
                        usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]
                    )
                    aluno.id = consulta[0]
                    self._usuario = aluno
                    return True
                else:
                    return False
        else:
            return False

    def logout(self):
        self._usuario = None


if __name__ == "__main__":
    import socket

    sistema = SistemaEducacional()
    host = 'localhost'
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
                if sistema.login(email, senha):
                    enviar = '1'
                    print(f'Usuário {email} efetuou o login no sistema')
                else:
                    enviar = '0'
                    print('Erro no login')
                con.send(enviar.encode())
            elif mensagem_str[0] == '2':
                email = mensagem_str[1]
                senha = mensagem_str[2]
                nome = mensagem_str[3]
                sobrenome = mensagem_str[4]
                nascimento = mensagem_str[5]
                enviar = ''
                if mensagem_str[-1] == 'a':
                    if sistema.cadastrar_aluno(email, senha, nome, sobrenome, nascimento):
                        enviar = '1'
                        print(f'Aluno {sistema.usuario} cadastrado no sistema')
                    else:
                        enviar = '0'
                        print('Erro ao cadastrar aluno no sistema')
                else:
                    if sistema.cadastrar_professor(email, senha, nome, sobrenome, nascimento):
                        enviar = '1'
                        print(f'Professor {sistema.usuario} cadastrado no sistema')
                    else:
                        enviar = '0'
                        print('Erro ao cadastrar professor no sistema')
                con.send(enviar.encode())
            elif mensagem_str[0] == '0':
                print(f'Usuário {sistema.usuario} deslogou')
                sistema.logout()
            else:
                raise Exception('Conexão finalizada pelo cliente')
        except Exception as e:
            print(str(e))
            con.close()
            serv_socket.close()
            break