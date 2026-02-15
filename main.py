class Pessoa:
    def __init__(self, nome, dataDeNascimento):
        self.nome = nome
        self.dataDeNascimento = dataDeNascimento
        
    def cadastrar(self):
        print(f"{self.nome} nascimento em: {self.dataDeNascimento}")
        print("Você foi cadastrado com sucesso!")
        
class Aluno(Pessoa):
    def __init__(self, nome, dataDeNascimento, turma):
        super().__init__(nome, dataDeNascimento)
        self.turma = turma
        
    def cadastrar(self):
        print(f"{self.nome} nascido em: {self.dataDeNascimento} da turma {self.turma}.")
        print("Você foi cadastrado com sucesso!")
        
class Professor(Pessoa):
    def __init__(self, nome, dataDeNascimento, disciplina):
        super().__init__(nome, dataDeNascimento)
        self.disciplina = disciplina
        
    def cadastrar(self):
        print(f"{self.nome} nascido em: {self.dataDeNascimento} lecionando {self.disciplina}.")
        print("Cadastro realizado com sucesso!")
        
print("Escolha a Opção desejada para cadastro: ")
opcao = input("1 - Professor. 2 - Aluno")

if opcao == 1:
    
