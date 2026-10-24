class Pessoa:
    def __init__(self, nome):
        self.nome = nome 
        
    def apresentar(self):
        return f"\nMeu nome é {self.nome}!"
    
class Aluno(Pessoa):
    def __init__(self, nome, turma):
        super().__init__(nome)
        self.turma = turma
        
    def info(self):
        return f"{super().apresentar()} | Turma: {self.turma}"
    
class Professor(Pessoa):
    def __init__(self, nome, uc, ch):
        super().__init__(nome)
        self.uc = uc 
        self.ch = ch 
    
    def info(self):
        return f"{super().apresentar()} | UC: {self.uc} | CH: {self.ch}h"
    

a = Aluno("Eduardo", "SNH8792")
p = Professor("Gerson", "Interface Gráfica", 96)

print(a.info())
print(p.info())