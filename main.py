class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
    def cadastrar(self):
        print(f"{self.nome}, R${self.valor}")
        print("Cadastrado com sucesso!")
        
class ProdutoAlimenticio(Produto):
    def __init__(self, nome, valor, validade):
        super().__init__(nome, valor)
        self.validade = validade
        
    def cadastrar(self):
        print(f"{self.nome}, R${self.valor}, validade: {self.validade}")
        print("Produto alimenticio cadastrado com sucesso!")

p1 = Produto("Notebook", 3499.90)
p1.cadastrar()

p2 = ProdutoAlimenticio("Arroz", 5.59, "12/04/2026")
p2.cadastrar()    
    