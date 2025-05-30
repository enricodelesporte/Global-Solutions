#Criando a classe de Contato de Emergência com seus atributos e construtores.
class ContatoEmergencia:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    #Exibindo informações    
    def __str__(self):
        return f" Contato de emergência: {self.nome} - Telefone: {self.telefone}"