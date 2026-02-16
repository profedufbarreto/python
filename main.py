class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos!")
        
class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} e tirei {self.nota}.")
        
class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} e ganho R${self.salario}.")
        
print("\nEscolha um valor: ")
print("1 - Para Pessoa Física: ")
print("2 - Para Aluno: ")
print("3 - Para Professor: ")
opcao = int(input("Opção desejada: "))

if opcao == 1:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    pessoa = Pessoa(nome, idade)
    pessoa.apresentar()
elif opcao == 2:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    nota = input("Digite a nota: ")
    aluno = Aluno(nome, idade, nota)
    aluno.apresentar()
elif opcao == 3:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    salario = input("Digite o salário: ")
    professor = Professor(nome, idade, salario)
    professor.apresentar()
else:
    print("Valor digitado inválido!")