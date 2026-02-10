def calcular_media(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    return soma / quantidade

lista = [10, 20, 30, 40]
print(calcular_media(lista))