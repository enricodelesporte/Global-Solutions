class RegiaoRisco:
    def __init__(self, estado, cidade, tipoRisco, nivelGravidade, ultimoRegistro):
        self.estado = estado
        self.cidade = cidade
        self.tipoRisco = tipoRisco
        self.nivelGravidade = nivelGravidade
        self.ultimoRegistro = ultimoRegistro

    def __str__(self):
        return f"{self.cidade} - {self.estado} | Tipo: {self.tipoRisco} | Nivel de gravidade: {self.nivelGravidade} | Ultimo registro: {self.ultimoRegistro}"