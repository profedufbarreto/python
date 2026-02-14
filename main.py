class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
    def cadastrar(self):
        print(f"{self.nome}, R${self.valor}")
        print("Cadastrado com sucesso!")
        

p1 = Produto("Arroz", 5.59)
p1.cadastrar()    
    