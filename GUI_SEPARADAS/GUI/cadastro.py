class Cadastro ():
    def __init__(self) -> None:
        self._lista_pessoas = []
    def add_pessoa(self, pessoa):
        existe = self.busca(pessoa.cpf)
        if (existe == None):
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False
    def busca (self,cpf):
        for c in self._lista_pessoas:
            if (c.cpf == cpf):
                return c
        return None
