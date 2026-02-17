soma = 0

num = int(input("Digite um número (0 para sair): "))

while num != 0:
    if num % 2 == 0:
        soma = soma + num
    num = int(input("Digite um número (0 para sair): "))

print(f"A soma dos números pares é {soma}")
