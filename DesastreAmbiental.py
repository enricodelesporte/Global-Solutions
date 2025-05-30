#Criando classe de Desastre Ambiental com seus atributos e construtores 
class DesastreAmbiental:
    def __init__(self, nome, descricao, nivel, local):
        self.nome = nome
        self.descricao = descricao
        self.nivel = nivel
        self.local = local

    def __str__(self):
        return f"Desastre: {self.nome} - Nível: {self.nivel} - Local: {self.local} | Descrição: {self.descricao}"