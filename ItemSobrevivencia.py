class ItemSobrevivencia:
    def __init__(self, nome, descricao, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade

    def __str__(self):
        return f"Item: {self.nome} - Quantidade: {self.quantidade} | Descrição: {self.descricao}"