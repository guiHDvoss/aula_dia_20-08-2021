from Contato import Contato

class Agenda:
    def __init__(self, nome_proprietario, ano):
        self.__nome_proprietario = nome_proprietario
        self.__ano = ano

    def getNomeproduto(self):
        return self.__nome_proprietario

    def getAno(self):
        return self.__ano

