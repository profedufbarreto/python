num = int(input("Digite um número: "))

if num < 0:
    print("Digitação inválida!")
else:
    if num % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")