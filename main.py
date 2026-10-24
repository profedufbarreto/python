class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario = salario
    
    def info(self):
        return f"{self.nome} | Salário: R${self.salario:.2f}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        
    def info(self):
        return f"{super().info} | Bônus: R${self.bonus:.2f}"
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
        
    def info(self):
        return f"{super().info()} | Linguagem: {self.linguagem}"
            
f = Funcionario("Ana", 3000)
g = Gerente("Carlos", 800, 1500)
d = Desenvolvedor("Lucas", 6000, "Python")

print(f.info())
print(g.info())
print(d.info())    