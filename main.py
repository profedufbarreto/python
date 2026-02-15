class Veiculo:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo 
        self.ano = ano
        self.cor = cor
    
    def cadastrar(self):
        prinf(f"{self.modelo} do ano {self.ano} na cor {self.cor}.")
        prinf(f"Foi cadastrado com sucesso!")
        
class Moto(Veiculo):
    def __init__(self, modelo, ano, cor):
        super().__init__(modelo, ano, cor)
        self.rodas = rodas
        
    def cadastrar(self):
        print(f"{self.modelo} do ano {self.ano} na cor {self.cor} possuindo {self.rodas} rodas.")
        print("Foi cadastrado com sucesso!")
        
tipo = input("Digite o tipo de veículo: ")

modelo = input("Digite o modelo do veículo: ")
ano = input("Digite o ano do veículo: ")
cor = input("Digite a cor do veículo: ")

if tipo.lower() == "moto":
    rodas = input("Digite a quantidade de rodas: ")
    vehichle = Moto(modelo, ano, cor, rodas)
else:
    vehichle = Veiculo(modelo, ano, cor)
    
vehichle.cadastrar()
        