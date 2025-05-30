class Usuario:
    #Criando os atributos que "Usuário" vai receber e armazenar
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.mochila = []
    
    #Exibição do nome e email do Usuário
    def __str__(self):
        return f"Usuário: {self.nome} | Email: {self.email}"



