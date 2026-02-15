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
        
p1 = Aluno("Eduardo", "11/07/1987", "321")
p1.cadastrar()