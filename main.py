class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
    def cadastrar(self):
        print(f"O {self.modelo} de {self.ano} e na cor {self.cor}foi cadastrado com sucesso!")
        
car1 = Carro("Corcel", 73, "Vermelha")
car1.cadastrar()