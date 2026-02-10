numeros = []


def subt(a, b):
    resultado = a - b 
    return resultado

def mult(a, b):
    resultado = a * b
    return resultado

def div(a, b):
    resultado = a / b
    return resultado

print("---------- Escolha a opção ----------")
opcao = int(input("Digite um valor para a operação correspondente: "))
print("1 - Para soma")
print("2 - Para subtração")
print("3 - Para multiplicação")
print("4 - Para divisão")

print(soma(5, 3))
print(subt(8, 2))
print(mult(8, 9))
print(div(18, 9))

for i in range(5):
    valor = int(input(f"Digite o número {i+1}: "))
    numeros.append(valor)
    
print("Lista final: ", numeros)

