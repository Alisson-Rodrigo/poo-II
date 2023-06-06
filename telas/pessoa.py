class Pessoa:
    def __init__(self, nome, endereco, email, usuario, nascimento, senha, confirmar_senha, plano_assinatura):
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._nascimento = nascimento
        self._usuario = usuario
        self._senha = senha
        self._confirmar_senha = confirmar_senha
        self._plano_assinatura = plano_assinatura

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def confirmar_senha(self):
        return self._confirmar_senha

    @confirmar_senha.setter
    def confirmar_senha(self, confirmar_senha):
        self._confirmar_senha = confirmar_senha

    @property
    def plano_assinatura(self):
        return self._plano_assinatura
