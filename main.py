from Contato import Contato
from Agenda import Agenda
from Tarefas import Tarefas

class Menu:
    def __init__(self):
        self.contato = []


    def Cadastrar_contato(self):
        nome = input('Digite o nome: ')
        telefone = input('Digite o número do telefone: ')
        email = input('Digite o email para contato: ')
        novo_contato = Contato(nome, telefone, email)
        self.contato.append(novo_contato)

    def listar_contato(self):

