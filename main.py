class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def apresentar(self):
        print(f"\nOlá, meu nome é {self.nome} e tenho {self.idade} anos.")
        print(f"Minha altura é de {self.altura}m.")
        
    def e_maior_de_idade(self):
        return self.idade >= 18
    
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

p = Pessoa(nome, idade, altura)
p.apresentar()

if p.e_maior_de_idade():
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")