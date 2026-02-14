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


nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))



p1 = Produto(nome, valor)
p1.cadastrar()