

class User:
    def __init__(self, usuario, nome, senha):
        self._usr = usuario
        self._name = nome
        self._senha = senha

    # getters
    def getusr(self):
        return self._usr

    def getname(self):
        return self._name

    def getsenha(self):
        return self._senha
