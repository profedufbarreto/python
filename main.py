nomes = ["Eduardo", "Brian", "Gabriel"]

nomeProcurado = input("Digite o nome: ")

if nomeProcurado in nomes:
    print(f"{nomeProcurado} está na lista!")
else:
    print(f"{nomeProcurado} não está na lista!")