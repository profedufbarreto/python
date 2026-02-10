def saudacao(nome, idade, cidade):
    print(f"Olá {nome}!")
    print(f"Você tem {idade} e mora em {cidade}!")
    
    
saudacao.nome = input("Digite seu nome: ")
saudacao.idade = input("Digite sua idade: ")
saudacao.cidade = input("Digite sua cidade: ")

print(saudacao.nome, saudacao.idade, saudacao.cidade)
print(saudacao.nome)
print(saudacao.idade)
print(saudacao.cidade)


