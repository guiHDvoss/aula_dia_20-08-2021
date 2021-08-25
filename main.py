from Contato import Contato
from Agenda import Agenda
from Tarefas import Tarefas

class Menu:
    def __init__(self):
        self.contato = []


    def Cadastrar_contato(self):
        nome = input('Digite o nome: ')
        numero_telefone = input('Digite o número do telefone: ')
        email_contato = input('Digite o email para contato: ')
        novo_contato = Contato(nome, numero_telefone, email_contato)
        self.contato.append(novo_contato)

    def listar_contato(self):
        print('Seu número de contatos é: ' + str(self.contato))

