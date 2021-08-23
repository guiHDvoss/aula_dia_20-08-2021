class Contato:
    def __init__(self, nome, numero_telefone, email_contato):
        self.__nome= nome
        self.__numero_telefone= numero_telefone
        self.__email_contato= email_contato

    def getNome(self):
        return self.__nome

    def getNumero_telefone(self):
        return self.__numero_telefone

    def getEmail_ccontato(self):
        return self.__email_contato

