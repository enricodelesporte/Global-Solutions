class MochilaSobrevivencia:
    def __init__(self, nome, descricao, categoria,):
        self.nome = nome 
        self.descricao = descricao
        self.categoria = categoria
        self.itens = []
    
    def adicionarItem (self, item):
        self.itens.append(item)

    def listarItens(self):
        for item in self.itens:
            print(item)

    def __str__(self):
        return f"Mochila: {self.nome} - Categoria: {self.categoria} | Descrição: {self.descricao}"