class Tarefas:
    def __init__(self, descricao, status):
        self.__descricao = descricao
        self.__status = status

    def getDescricao_tarefa(self):
        return self.__descricao

    def getStatus(self):
        return self.__status
